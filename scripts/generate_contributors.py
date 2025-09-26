#!/usr/bin/env python3
"""
Script ajustado para gerar contributors.md no formato que funciona
"""

import requests
import os

def get_contributors(repo_owner, repo_name):
    """Busca e ordena contribuidores por número de commits"""
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contributors"
    response = requests.get(url)
    
    if response.status_code == 200:
        contributors = response.json()
        # Ordena por número de commits (decrescente)
        contributors.sort(key=lambda x: x['contributions'], reverse=True)
        return contributors
    else:
        print(f"Erro ao buscar contribuidores: {response.status_code}")
        return []

def generate_contributors_html(contributors):
    """Gera HTML no formato que funciona com Marmite"""
    if not contributors:
        return """# Contributors\n\n*Ainda não há contribuidores. Seja o primeiro!*"""
    
    html = '''# Contribuidores

<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;">
'''
    
    for contributor in contributors:
        username = contributor['login']
        avatar_url = contributor['avatar_url']
        commits = contributor['contributions']
        profile_url = f"https://github.com/{username}"
        
        html += f'''
<div style="width: 250px; text-align: center; padding: 20px; border: 1px solid #ddd; border-radius: 8px; background: #f9f9f9;">
    <h3 style="margin: 0 0 15px 0;">
        <a href="{profile_url}" target="_blank" style="text-decoration: none; color: #0366d6;">{username}</a>
    </h3>
    <a href="{profile_url}" target="_blank">
        <img src="{avatar_url}" style="width: 100px; height: 100px; border-radius: 50%;">
    </a>
    <p style="margin: 15px 0 0 0; color: #666;">{commits} commit{'' if commits == 1 else 's'}</p>
</div>
'''
    
    html += '</div>'
    return html

def main():
    repo_owner = "waltenne"
    repo_name = "mini-curso-cicd"
    
    print("Buscando contribuidores...")
    contributors = get_contributors(repo_owner, repo_name)
    
    if contributors:
        print(f"Encontrados {len(contributors)} contribuidores")
        content = generate_contributors_html(contributors)
        
        with open("content/contributors.md", 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("Arquivo contributors.md atualizado!")
        
        # Mostra preview dos contribuidores encontrados
        print("\nContribuidores encontrados:")
        for i, contributor in enumerate(contributors[:5], 1):
            print(f"{i}. {contributor['login']} - {contributor['contributions']} commits")
        
        if len(contributors) > 5:
            print(f"... e mais {len(contributors) - 5} contribuidores")
            
    else:
        print("Nenhum contribuidor encontrado")

if __name__ == "__main__":
    main()