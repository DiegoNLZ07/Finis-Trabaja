<template>
  <div class="bg-light min-vh-100">
    <nav class="navbar navbar-expand-lg navbar-dark shadow-sm" style="background-color: #003366;">
      <div class="container">
        <a class="navbar-brand d-flex align-items-center" href="#" style="font-size: 1.5rem;">
          <img src="/logo-uft.png" alt="Logo Universidad" width="45" height="45" class="me-3">
          <div class="d-flex align-items-baseline">
            <span class="fw-bolder text-white" style="letter-spacing: 1px;">FINIS</span>
            <span class="fw-light ms-2" style="color: #48CAE4; letter-spacing: 2px;">TRABAJA</span>
          </div>
        </a>
        <div class="d-flex gap-2">
          <button 
            @click="vistaActual = 'empresa'" 
            :class="['btn fw-semibold', vistaActual === 'empresa' ? 'btn-light text-dark shadow-sm' : 'btn-outline-light border-0']">
            🏢 Modo Empresa
          </button>
          <button 
            @click="vistaActual = 'estudiante'" 
            :class="['btn fw-semibold', vistaActual === 'estudiante' ? 'btn-warning text-dark shadow-sm' : 'btn-outline-light border-0']">
            🎓 Modo Estudiante
          </button>
        </div>
      </div>
    </nav>

    <div class="bg-white text-center py-5 mb-4 border-bottom shadow-sm">
      <div class="container py-3">
        <h1 class="display-4 fw-bold text-dark mb-3">
          Impulsa tu <span style="color: #003366;">Futuro Profesional</span>
        </h1>
        <p class="lead text-muted mx-auto" style="max-width: 700px;">
          La plataforma exclusiva para vincular el talento de nuestra universidad con las mejores oportunidades del mercado laboral.
        </p>
      </div>
    </div>

    <main class="pb-5">
      <transition name="fade" mode="out-in">
        <VistaEmpresa v-if="vistaActual === 'empresa'" />
        <VistaEstudiante v-else />
      </transition>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import VistaEmpresa from './views/VistaEmpresa.vue';
import VistaEstudiante from './views/VistaEstudiante.vue';

// Por defecto arranca en modo empresa
const vistaActual = ref('empresa');
</script>

<style scoped>
/* Animación suave al cambiar entre Empresa y Estudiante */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>