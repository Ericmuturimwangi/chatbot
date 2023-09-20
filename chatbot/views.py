from django.shortcuts import render
from django.http import JsonResponse
import openai

# Create your views here.

openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    response=openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    print(response)
        #answer = response.choice[0].text.strip()
        #return answer


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = 'Hello this is my response'
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')
    

