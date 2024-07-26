from django.shortcuts import render, redirect
import requests
from django.conf import settings
from django.db.models import Q

headers = {
    'Authorization': f'Token {settings.API_TOKEN}'
}

def index(request):
    return render(request, 'research_frontend/index.html')

def researches(request):
    response = requests.get(f'{settings.API_URL}/research/', headers=headers)
    researches = response.json()
    return render(request, 'research_frontend/researches.html', {'researches': researches})

def researchers(request):
    response = requests.get(f'{settings.API_URL}/researcher/', headers=headers)
    researchers = response.json()
    return render(request, 'research_frontend/researchers.html', {'researchers': researchers})

def publications(request):
    response = requests.get(f'{settings.API_URL}/publication/', headers=headers)
    publications = response.json()
    return render(request, 'research_frontend/publications.html', {'publications': publications})

def research(request, id):
    response = requests.get(f'{settings.API_URL}/research/{id}/', headers=headers)
    research = response.json()
    response2 = requests.get(f'{settings.API_URL}/researcher/{research["researcher"]}/', headers=headers)
    researcher = response2.json()
    research['researcher'] = researcher
    return render(request, 'research_frontend/research.html', {'research': research})

def researcher(request, id):
    response = requests.get(f'{settings.API_URL}/researcher/{id}/', headers=headers)
    researcher = response.json()
    response2 = requests.get(f'{settings.API_URL}/research/?researcher={id}', headers=headers)
    researches = response2.json()
    researcher['researches'] = researches
    return render(request, 'research_frontend/researcher.html', {'researcher': researcher})

def publication(request, id):
    response = requests.get(f'{settings.API_URL}/publication/{id}/', headers=headers)
    publication = response.json()
    response2 = requests.get(f'{settings.API_URL}/research/{publication["research"]}/', headers=headers)
    research = response2.json()
    publication['research'] = research
    return render(request, 'research_frontend/publication.html', {'publication': publication})

def delete_research(request, id):
    response = requests.delete(f'{settings.API_URL}/research/{id}/', headers=headers)
    return redirect('research_frontend:researches')

def delete_researcher(request, id):
    response = requests.delete(f'{settings.API_URL}/researcher/{id}/', headers=headers)
    return redirect('research_frontend:researchers')

def delete_publication(request, id):
    response = requests.delete(f'{settings.API_URL}/publication/{id}/', headers=headers)
    return redirect('research_frontend:publications')

def create_research(request):
    response = requests.get(f'{settings.API_URL}/researcher/', headers=headers)
    researchers = response.json()
    if request.method == 'POST':
        data = {
            'title': request.POST['title'],
            'description': request.POST['description'],
            'start_date': request.POST['start_date'],
            'end_date': request.POST['end_date'],
            'researcher': request.POST['researcher']
        }
        response = requests.post(f'{settings.API_URL}/research/', data=data, headers=headers)
        return redirect('research_frontend:researches')
    return render(request, 'research_frontend/create_research.html', {'researchers': researchers})

def create_researcher(request):
    response = requests.get(f'{settings.API_URL}/research/', headers=headers)
    researches = response.json()
    if request.method == 'POST':
        data = {
            'name': request.POST['name'],
            'specialty': request.POST['specialty'],
            'research': request.POST['researches']
        }
        response = requests.post(f'{settings.API_URL}/researcher/', data=data, headers=headers)
        return redirect('research_frontend:researchers')
    return render(request, 'research_frontend/create_researcher.html', {'researches': researches})

def create_publication(request):
    response = requests.get(f'{settings.API_URL}/research/', headers=headers)
    researches = response.json()
    if request.method == 'POST':
        data = {
            'title': request.POST['title'],
            'summary': request.POST['summary'],
            'publication_date': request.POST['publication_date'],
            'research': request.POST['research']
        }
        response = requests.post(f'{settings.API_URL}/publication/', data=data, headers=headers)
        return redirect('research_frontend:publications')
    return render(request, 'research_frontend/create_publication.html', {'researches': researches})

def update_research(request, id):
    response = requests.get(f'{settings.API_URL}/research/{id}/', headers=headers)
    research = response.json()
    response2 = requests.get(f'{settings.API_URL}/researcher/', headers=headers)
    researchers = response2.json()
    if request.method == 'POST':
        data = {
            'title': request.POST['title'],
            'description': request.POST['description'],
            'start_date': request.POST['start_date'],
            'end_date': request.POST['end_date'],
            'researcher': request.POST['researcher']
        }
        response = requests.put(f'{settings.API_URL}/research/{id}/', data=data, headers=headers)
        return redirect('research_frontend:researches')
    return render(request, 'research_frontend/update_research.html', {'research': research, 'researchers': researchers})

def update_researcher(request, id):
    response = requests.get(f'{settings.API_URL}/researcher/{id}/', headers=headers)
    researcher = response.json()
    response2 = requests.get(f'{settings.API_URL}/research/', headers=headers)
    researches = response2.json()
    if request.method == 'POST':
        data = {
            'name': request.POST['name'],
            'specialty': request.POST['specialty']
        }
        response = requests.put(f'{settings.API_URL}/researcher/{id}/', data=data, headers=headers)
        return redirect('research_frontend:researchers')
    return render(request, 'research_frontend/update_researcher.html', {'researcher': researcher, 'researches': researches})

def update_publication(request, id):
    response = requests.get(f'{settings.API_URL}/publication/{id}/', headers=headers)
    publication = response.json()
    response2 = requests.get(f'{settings.API_URL}/research/', headers=headers)
    researches = response2.json()
    if request.method == 'POST':
        data = {
            'title': request.POST['title'],
            'summary': request.POST['summary'],
            'publication_date': request.POST['publication_date'],
            'research': request.POST['research']
        }
        response = requests.put(f'{settings.API_URL}/publication/{id}/', data=data, headers=headers)
        return redirect('research_frontend:publications')
    return render(request, 'research_frontend/update_publication.html', {'publication': publication, 'researches': researches})

def filter(request):
    response2 = requests.get(f'{settings.API_URL}/researcher/', headers=headers)
    researchers = response2.json()
    if request.GET:
        title = request.GET.get('title')
        start_date = request.GET.get('start_date')
        researcher = request.GET.get('researcher')

        filters = Q()
        if title != '':
            filters &= Q(title=title)
        if start_date != '':
            filters &= Q(start_date=start_date)
        if researcher != '':
            filters &= Q(researcher=researcher)
        
        response = requests.get(f'{settings.API_URL}/research/?{str(filters)}', headers=headers)
        researches = response.json()
        return render(request, 'research_frontend/researches.html', {'researches': researches, 'filters': filters})
    return render(request, 'research_frontend/filter.html', {'researchers': researchers})

def visualization(request):
    return render(request, 'research_frontend/visualization.html')

def chatbot(request):
    return render(request, 'research_frontend/chatbot.html')