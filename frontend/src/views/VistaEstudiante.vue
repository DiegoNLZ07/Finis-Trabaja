<template>
  <div class="container">
    <div class="card shadow-sm border-0">
      <div class="card-header bg-white border-bottom-0 pt-4 pb-0 d-flex justify-content-between align-items-center">
        <h2 class="h4 text-dark mb-0">Ofertas Disponibles</h2>
        <button @click="cargarOfertas" class="btn btn-sm btn-outline-secondary">
          🔄 Actualizar Ofertas
        </button>
      </div>
      <div class="card-body">
        <p class="text-muted small mb-4">Vacantes a las que aún no has postulado (Estudiante ID: 2)</p>

        <div v-if="ofertas.length > 0" class="row g-4">
          <div v-for="oferta in ofertas" :key="oferta.id" class="col-12">
            <div class="d-flex justify-content-between align-items-center p-3 border rounded shadow-sm bg-white">
              <div>
                <h5 class="text-primary mb-1">{{ oferta.titulo_cargo }}</h5>
                <p class="text-muted mb-0">{{ oferta.descripcion }}</p>
              </div>
              <button @click="postular(oferta.id)" class="btn btn-success fw-semibold ms-3">
                📩 Postular
              </button>
            </div>
          </div>
        </div>

        <div v-else class="alert alert-warning text-center" role="alert">
          ¡Felicidades! Ya has postulado a todas las ofertas disponibles en la base de datos.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const ofertas = ref([]);
const ESTUDIANTE_ID = 2;
const API_URL = "http://localhost:8000";

const cargarOfertas = async () => {
  try {
    const res = await fetch(`${API_URL}/estudiantes/${ESTUDIANTE_ID}/ofertas`);
    if (res.ok) {
      ofertas.value = await res.json();
    }
  } catch (error) {
    console.error("Error conectando a la BD:", error);
  }
};

const postular = async (ofertaId) => {
  try {
    const res = await fetch(`${API_URL}/estudiantes/${ESTUDIANTE_ID}/postular/${ofertaId}`, {
      method: 'POST'
    });
    if (res.ok) {
      // Recargamos la lista desde la BD. Como la postulación ya existe, 
      // el backend filtrará esta oferta y ya no aparecerá en la pantalla.
      await cargarOfertas();
    }
  } catch (error) {
    console.error("Error al postular:", error);
  }
};

onMounted(() => {
  cargarOfertas();
});
</script>