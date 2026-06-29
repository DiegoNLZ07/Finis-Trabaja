<template>
  <div class="container mt-4">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="text-primary">Mis Ofertas Publicadas</h2>
      <button @click="cargarDatos" class="btn btn-outline-primary">↻ Refrescar Datos</button>
    </div>

    <div v-if="cargando" class="spinner-border text-primary" role="status"></div>
    
    <div v-else class="table-responsive">
      <table class="table table-bordered table-hover shadow-sm">
        <thead class="table-light">
          <tr>
            <th>ID</th>
            <th>Título del Cargo</th>
            <th>Empresa</th>
            <th>Modalidad</th>
            <th>Sueldo</th>
            <th>Estado</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="oferta in ofertas" :key="oferta.id">
            <td>{{ oferta.id }}</td>
            <td class="fw-bold">{{ oferta.titulo }}</td>
            <td>{{ oferta.empresa }}</td>
            <td>{{ oferta.modalidad }}</td>
            <td>{{ oferta.sueldo }}</td>
            <td><span class="badge bg-success">Activa</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { useOfertasController } from '../controllers/OfertasController';
const { ofertas, cargando, cargarDatos } = useOfertasController();
</script>