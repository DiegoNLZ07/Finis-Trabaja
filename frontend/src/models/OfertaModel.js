export default class OfertaModel {
  // Esta función buscará los datos en tu API (FastAPI)
  static async obtenerOfertas() {
    try {
      // Simulación de respuesta de FastAPI (el backend de Matías)
      return [
        { id: 1, titulo: "Desarrollador Vue.js", empresa: "VexZeta", sueldo: "$900.000", modalidad: "Remoto" },
        { id: 2, titulo: "Practicante Informática", empresa: "UFT", sueldo: "$200.000", modalidad: "Presencial" }
      ];
    } catch (error) {
      console.error("Error conectando con el backend:", error);
      return [];
    }
  }
}