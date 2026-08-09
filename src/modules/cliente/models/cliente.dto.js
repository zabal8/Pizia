class ClienteRequest {
  constructor(data) {
    this.nombre = data.nombre;
    this.email = data.email;
  }

  validate() {
    const errors = [];

    if (!this.nombre || typeof this.nombre !== 'string') {
      errors.push('El nombre es obligatorio');
    }

    if (!this.email || typeof this.email !== 'string') {
      errors.push('El email es obligatorio');
    }

    return errors;
  }
}

class ClienteResponse {
  constructor(cliente) {
    this.id = cliente.id;
    this.nombre = cliente.nombre;
    this.email = cliente.email;
    this.createdAt = cliente.createdAt;
    this.updatedAt = cliente.updatedAt;
  }
}

module.exports = {
  ClienteRequest,
  ClienteResponse
};