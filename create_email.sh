#!/bin/bash
docker-compose exec mailserver setup email add $1 $2
