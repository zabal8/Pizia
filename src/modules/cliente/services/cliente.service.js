const db = require('../../../database/database');
const { Cliente } = require('../models/cliente.model');

class ClienteService {

  findAll() {
    const rows = db.prepare(`
      SELECT
        id,
        nombre,
        email,
        created_at AS createdAt,
        updated_at AS updatedAt
      FROM clientes
    `).all();

    return rows;
  }

  findById(id) {
    const row = db.prepare(`
      SELECT
        id,
        nombre,
        email,
        created_at AS createdAt,
        updated_at AS updatedAt
      FROM clientes
      WHERE id = ?
    `).get(id);

    if (!row) {
      throw new Error(`Cliente con ID ${id} no encontrado`);
    }

    return row;
  }

  save(data) {
    const existe = db.prepare(`
      SELECT id
      FROM clientes
      WHERE email = ?
    `).get(data.email);

    if (existe) {
      throw new Error('Ya existe un cliente con ese email');
    }

    const cliente = new Cliente(data);

    db.prepare(`
      INSERT INTO clientes (
        id,
        nombre,
        email,
        created_at,
        updated_at
      )
      VALUES (?, ?, ?, ?, ?)
    `).run(
      cliente.id,
      cliente.nombre,
      cliente.email,
      cliente.createdAt,
      cliente.updatedAt
    );

    return cliente;
  }

  update(id, data) {
    const clienteActual = this.findById(id);

    const clienteActualizado = {
      ...clienteActual,
      ...data,
      id: clienteActual.id,
      createdAt: clienteActual.createdAt,
      updatedAt: new Date().toISOString()
    };

    db.prepare(`
      UPDATE clientes
      SET
        nombre = ?,
        email = ?,
        updated_at = ?
      WHERE id = ?
    `).run(
      clienteActualizado.nombre,
      clienteActualizado.email,
      clienteActualizado.updatedAt,
      id
    );

    return clienteActualizado;
  }

  delete(id) {
    const resultado = db.prepare(`
      DELETE FROM clientes
      WHERE id = ?
    `).run(id);

    if (resultado.changes === 0) {
      throw new Error(`Cliente con ID ${id} no encontrado`);
    }
  }
}

module.exports = new ClienteService();