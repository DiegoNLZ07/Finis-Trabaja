// src/controllers/OfertasController.js
import { ref, onMounted } from 'vue';
import OfertaModel from '../models/OfertaModel';

export const useOfertasController = () => {
  const ofertas = ref([]);
  const cargando = ref(true);

  const cargarDatos = async () => {
    cargando.value = true;
    ofertas.value = await OfertaModel.obtenerOfertas();
    cargando.value = false;
  };

  const tomarOferta = async (idOferta) => {
    const exito = await OfertaModel.postularOferta(idOferta);
    if (exito) {
      // Como pide la rúbrica: "Si el estudiante postula, esta ya no debe mostrarse"
      await cargarDatos(); 
    }
  };

  onMounted(() => {
    cargarDatos();
  });

  return { 
    ofertas, 
    cargando, 
    cargarDatos, 
    tomarOferta 
  };
};