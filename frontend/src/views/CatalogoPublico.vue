<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Ofertas Laborales Finis Trabaja</h1>
    
    <div v-if="cargando" class="text-gray-500">Cargando...</div>
    
    <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div v-for="o in ofertas" :key="o.id" class="border p-4 rounded shadow">
        <h2 class="font-bold text-xl">{{ o.titulo }}</h2>
        <p class="text-blue-600">{{ o.empresa }}</p>
        <p>Renta: {{ o.sueldo }} | Modalidad: {{ o.modalidad }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useOfertasController } from '../controllers/useOfertasController';
const { ofertas, cargando } = useOfertasController();
</script>