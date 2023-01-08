#!/bin/bash

docker-compose exec mailserver setup email add admin@casualpv.online admin
docker-compose exec mailserver setup alias add postmaster@casualpv.online admin@casualpv.online
docker-compose exec mailserver setup config dkim
