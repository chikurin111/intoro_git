#visionをインポート
from google.cloud import vision

#katou_megumi.jpgを開いて読み込む
with open('./uma_0001.png', 'rb') as image_file:
	content = image_file.read()

#vision APIが扱える画像データにする
image = vision.Image(content=content)

#print(image)

#ImageAnnotatorClientのインスタンスの生成
annotator_client = vision.ImageAnnotatorClient()

#response_data = annotator_client.label_detection(image=image)
response_data = annotator_client.document_text_detection(image=image)

#labels = response_data.label_annotations
texts = response_data.text_annotations

#for label in labels:
#	print(label.description, ':', round(label.score * 100, 1), '%')
for text in texts:
#	print('\n"{}"'.format(text.description))
	print('\n"{}"'.format(text.description))
#	vertices = (['({},{})'.format(vertex.x, vertex.y) for vertex in text.bounding_poly.vertices])
#	print('bounds: {}'.format(','.join(vertices)))