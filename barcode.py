import cv2
from pyzbar import pyzbar
cap = cv2.VideoCapture(0) # 0 for default webcam


while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    barcodes = pyzbar.decode(frame)
    
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type
    
        text = f"{barcode_data} ({barcode_type})"
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        print(f"Barcode: {barcode_data}, Type: {barcode_type}")
    cv2.imshow('Barcode Reader', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()