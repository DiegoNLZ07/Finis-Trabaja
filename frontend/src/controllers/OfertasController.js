import { ref, onMounted } from 'vue';
import OfertaModel from '../models/OfertaModel';

export function useOfertasController() {
  const ofertas = ref([]);
  const cargando = ref(true);

  const actualizarListado = async () => {
    cargando.value = true;
    ofertas.value = await OfertaModel.obtenerOfertas();
    cargando.value = false;
  };

  onMounted(actualizarListado);

  return { ofertas, cargando };
}