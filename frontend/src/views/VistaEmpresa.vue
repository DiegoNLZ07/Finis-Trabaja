<template>
  <div class="container">
    <div class="card shadow-sm border-0">
      <div class="card-header bg-white border-bottom-0 pt-4 pb-0 d-flex justify-content-between align-items-center">
        <h2 class="h4 text-dark mb-0">Mis Ofertas Publicadas</h2>
        <button @click="cargarOfertas" class="btn btn-sm btn-outline-secondary">
          🔄 Actualizar Lista
        </button>
      </div>
      <div class="card-body">
        <p class="text-muted small mb-4">Datos obtenidos en tiempo real de la base de datos (Empresa ID: 1)</p>
        
        <div v-if="ofertas.length > 0" class="row g-3">
          <div v-for="oferta in ofertas" :key="oferta.id" class="col-md-6">
            <div class="p-3 border rounded h-100 position-relative bg-light">
              <span class="badge bg-success position-absolute top-0 end-0 m-2">{{ oferta.estado }}</span>
              <h5 class="text-primary mb-1">{{ oferta.titulo_cargo }}</h5>
              <p class="text-secondary mb-0">{{ oferta.descripcion }}</p>
            </div>
          </div>
        </div>
        
        <div v-else class="alert alert-info text-center" role="alert">
          No tienes ofertas laborales registradas en la base de datos en este momento.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const ofertas = ref([]);
const EMPRESA_ID = 1;
const API_URL = "http://localhost:8000";

const cargarOfertas = async () => {
  try {
    const res = await fetch(`${API_URL}/empresas/${EMPRESA_ID}/ofertas`);
    if (res.ok) {
      ofertas.value = await res.json();
    }
  } catch (error) {
    console.error("Error conectando a la BD:", error);
  }
};

onMounted(() => {
  cargarOfertas();
});
</script>