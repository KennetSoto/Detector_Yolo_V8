from ultralytics import YOLO

# Cria uma instância do modelo YOLO, carregando o modelo 'yolov8n.pt' (versao leve do yolo, nano)
model = YOLO('yolov8n.pt')

# Realiza previsões utilizando o modelo carregado
# - source='0' indica que a fonte de entrada é '0', que pode representar a câmera padrão
model.predict(source='0', show=True)

#feche o terminal para encerrar a execução