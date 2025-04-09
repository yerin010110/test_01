from transformers import pipeline   # from transformers > transformers는 hugging face의 대표 python 라이브러리 입니다. 이 안의 pipline 함수는 복잡한 전처리/후처리 없이 바로 모델을 사용할 수 있게 해주는 간단한 실행 도구입니다. 
import gradio as gr

classifier = pipeline("sentiment-analysis")

def analyze(text):
    result = classifier(text)[0]
    return f"Label: {result['label']}, Score: {result['score']:.2f}"

iface = gr.Interface(fn=analyze, inputs="text", outputs="text")
iface.launch()


