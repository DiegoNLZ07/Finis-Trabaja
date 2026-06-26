// src/models/OfertaModel.js
export default class OfertaModel {
  // Simulamos los datos que vendrían de la BD de Matías
  static ofertasFalsas = [
    { id: 1, titulo: "Desarrollador Vue.js", empresa: "VexZeta", sueldo: "$900.000", modalidad: "Remoto" },
    { id: 2, titulo: "Practicante de Informática", empresa: "UFT Interno", sueldo: "$250.000", modalidad: "Presencial" },
    { id: 3, titulo: "Analista QA Junior", empresa: "Tech Solutions", sueldo: "$600.000", modalidad: "Híbrido" }
  ];

  static async obtenerOfertas() {
    // Aquí irá el Axios (GET) al backend. Por ahora, devolvemos la lista falsa.
    return [...this.ofertasFalsas];
  }

  static async postularOferta(idOferta) {
    // Aquí irá el Axios (POST) al backend.
    // Simulamos que la postulación fue exitosa eliminando la oferta de nuestra BD falsa.
    this.ofertasFalsas = this.ofertasFalsas.filter(oferta => oferta.id !== idOferta);
    return true;
  }
}