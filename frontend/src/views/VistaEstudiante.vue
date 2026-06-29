<template>
  <div class="container mt-4">
    <h2 class="text-success mb-4">Catálogo de Oportunidades</h2>

    <div v-if="mensajeExito" class="alert alert-success alert-dismissible fade show shadow-sm" role="alert">
      <strong>¡Excelente!</strong> {{ mensajeExito }}
      <button type="button" class="btn-close" @click="mensajeExito = ''"></button>
    </div>

    <div class="card mb-4 shadow-sm border-0 bg-light">
      <div class="card-body">
        <h5 class="card-title text-muted mb-3">Filtrar Ofertas</h5>
        <div class="row g-3">
          <div class="col-md-4">
            <input 
              v-model="filtroTitulo" 
              type="text" 
              class="form-control" 
              placeholder="Buscar por cargo (ej. Desarrollador)" 
            />
          </div>
          <div class="col-md-4">
            <input 
              v-model="filtroEmpresa" 
              type="text" 
              class="form-control" 
              placeholder="Buscar por empresa" 
            />
          </div>
          <div class="col-md-4">
            <select v-model="filtroModalidad" class="form-select">
              <option value="">Todas las modalidades</option>
              <option value="Remoto">Remoto</option>
              <option value="Híbrido">Híbrido</option>
              <option value="Presencial">Presencial</option>
            </select>
          </div>
        </div>
      </div>
    </div>

    <div v-if="cargando" class="spinner-border text-success" role="status">
      <span class="visually-hidden">Cargando...</span>
    </div>

    <div v-else-if="ofertasFiltradas.length === 0" class="alert alert-warning">
      No se encontraron ofertas que coincidan con tu búsqueda.
    </div>

    <div v-else class="row">
      <div v-for="oferta in ofertasFiltradas" :key="oferta.id" class="col-md-4 mb-4">
        <div class="card shadow-sm h-100 border-success border-opacity-25">
          <div class="card-body">
            <h5 class="card-title text-success">{{ oferta.titulo }}</h5>
            <h6 class="card-subtitle mb-3 text-muted">{{ oferta.empresa }}</h6>
            <ul class="list-unstyled mb-4">
              <li><strong>Modalidad:</strong> {{ oferta.modalidad }}</li>
              <li><strong>Renta:</strong> {{ oferta.sueldo }}</li>
            </ul>
            <button @click="procesarPostulacion(oferta.id)" class="btn btn-success w-100">
              Postular a esta oferta
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useOfertasController } from '../controllers/OfertasController';

// Extraemos lo necesario del controlador
const { ofertas, cargando, tomarOferta } = useOfertasController();

// Variables reactivas para los filtros
const filtroTitulo = ref('');
const filtroEmpresa = ref('');
const filtroModalidad = ref('');

// Variable para el mensaje de éxito
const mensajeExito = ref('');

// Lógica computada para filtrar las ofertas en tiempo real
const ofertasFiltradas = computed(() => {
  return ofertas.value.filter(oferta => {
    const coincideTitulo = oferta.titulo.toLowerCase().includes(filtroTitulo.value.toLowerCase());
    const coincideEmpresa = oferta.empresa.toLowerCase().includes(filtroEmpresa.value.toLowerCase());
    const coincideModalidad = filtroModalidad.value === '' || oferta.modalidad === filtroModalidad.value;
    
    return coincideTitulo && coincideEmpresa && coincideModalidad;
  });
});

// Función envoltorio para mostrar el mensaje tras postular
const procesarPostulacion = async (idOferta) => {
  // Llama a la función original del controlador
  await tomarOferta(idOferta);
  
  // Muestra el mensaje en la pantalla
  mensajeExito.value = "¡Postulación enviada! La empresa revisará tu CVV.";
  
  // Oculta el mensaje automáticamente después de 4 segundos
  setTimeout(() => {
    mensajeExito.value = '';
  }, 4000);
};
</script>