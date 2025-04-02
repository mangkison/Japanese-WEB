from django.shortcuts import render

def home(request):
    repos = [
        {'name': '포트폴리오', 'url': 'https://github.com/mangkison?tab=repositories'},
        {'name': 'AI 프로젝트', 'url': 'https://github.com/yourname/ai-project'},
    ]
    return render(request, 'home.html', {'repos': repos})