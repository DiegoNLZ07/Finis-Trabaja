<template>
  <div class="container">
    <div class="card shadow-sm border-0 mb-4 bg-light">
      <div class="card-body">
        <h3 class="h5 text-dark mb-3">Publicar Nueva Oferta</h3>
        <form @submit.prevent="crearOferta" class="row g-3 align-items-end">
          <div class="col-md-4">
            <label class="form-label text-muted small mb-1">Título del Cargo</label>
            <input v-model="nuevaOferta.titulo_cargo" type="text" class="form-control" placeholder="Ej. Ingeniero de Software" required>
          </div>
          <div class="col-md-6">
            <label class="form-label text-muted small mb-1">Descripción de la vacante</label>
            <input v-model="nuevaOferta.descripcion" type="text" class="form-control" placeholder="Ej. Experiencia en Python y Vue 3..." required>
          </div>
          <div class="col-md-2">
            <button type="submit" class="btn btn-primary w-100 fw-semibold" style="background-color: #003366; border: none;">
              ➕ Publicar
            </button>
          </div>
        </form>
      </div>
    </div>

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
            <div class="p-3 border rounded h-100 position-relative bg-white shadow-sm">
              <span class="badge position-absolute top-0 end-0 m-2" style="background-color: #48CAE4;">{{ oferta.estado }}</span>
              <h5 class="text-primary mb-1" style="color: #003366 !important;">{{ oferta.titulo_cargo }}</h5>
              <p class="text-secondary mb-0">{{ oferta.descripcion }}</p>
            </div>
          </div>
        </div>
        
        <div v-else class="alert alert-info text-center border-0" role="alert" style="background-color: #e2f4fb; color: #003366;">
          No tienes ofertas laborales registradas en la base de datos en este momento.
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const ofertas = ref([]);
// Estado para limpiar y enviar el formulario
const nuevaOferta = ref({
  titulo_cargo: '',
  descripcion: ''
});

const EMPRESA_ID = 1;
const API_URL = "http://localhost:8000";

// GET: Traer las ofertas
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

// POST: Crear la nueva oferta
const crearOferta = async () => {
  try {
    const res = await fetch(`${API_URL}/empresas/${EMPRESA_ID}/ofertas`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(nuevaOferta.value)
    });
    
    if (res.ok) {
      // Limpiamos los campos del formulario
      nuevaOferta.value = { titulo_cargo: '', descripcion: '' };
      // Recargamos la lista para que la oferta aparezca inmediatamente en pantalla
      await cargarOfertas();
    }
  } catch (error) {
    console.error("Error al crear oferta:", error);
  }
};

onMounted(() => {
  cargarOfertas();
});
</script>