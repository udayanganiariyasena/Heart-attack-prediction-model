#!/bin/bash

# Navigate to the app directory
cd /var/www/html/Heart-attack-prediction-model

echo "restarting service"
sudo systemctl status fastapi-app.service
echo "started service 🚀"