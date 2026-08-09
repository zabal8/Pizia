const clienteService = require('../services/cliente.service');

const {
  ClienteRequest,
  ClienteResponse
} = require('../models/cliente.dto');

class ClienteController {

  getAll(req, res) {
    try {
      const clientes = clienteService.findAll();

      const response = clientes.map(
        cliente => new ClienteResponse(cliente)
      );

      return res.status(200).json(response);

    } catch (error) {
      return res.status(500).json({
        message: error.message
      });
    }
  }

  getById(req, res) {
    try {
      const cliente = clienteService.findById(req.params.id);

      return res.status(200).json(
        new ClienteResponse(cliente)
      );

    } catch (error) {
      return res.status(404).json({
        message: error.message
      });
    }
  }

  create(req, res) {
    try {
      const request = new ClienteRequest(req.body);

      const errors = request.validate();

      if (errors.length > 0) {
        return res.status(400).json({
          errors: errors
        });
      }

      const cliente = clienteService.save(req.body);

      return res.status(201).json(
        new ClienteResponse(cliente)
      );

    } catch (error) {
      return res.status(409).json({
        message: error.message
      });
    }
  }

  update(req, res) {
    try {
      const cliente = clienteService.update(
        req.params.id,
        req.body
      );

      return res.status(200).json(
        new ClienteResponse(cliente)
      );

    } catch (error) {
      return res.status(404).json({
        message: error.message
      });
    }
  }

  delete(req, res) {
    try {
      clienteService.delete(req.params.id);

      return res.status(204).send();

    } catch (error) {
      return res.status(404).json({
        message: error.message
      });
    }
  }
}

module.exports = new ClienteController();