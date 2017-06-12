#!/usr/bin/env python

import connexion
from .encoder import JSONEncoder


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Clash of Cubicles is multiplayer RPG which simulates the Kafka-esque aspects of the cubicle rat-race, and the growth and reward of advancing up the hamster wheel faster than your peers.'})
    app.run(port=8080)
