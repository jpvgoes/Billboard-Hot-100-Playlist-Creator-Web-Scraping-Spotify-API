# Scraping the Billboard Hot 100 and Creating a Spotify Playlist

## Descrição do Projeto

Este projeto permite que o usuário viaje no tempo para um ano específico e crie uma playlist no Spotify com as músicas do **Billboard Hot 100** daquele ano. Ele utiliza as bibliotecas **BeautifulSoup**, **Requests** e **Spotipy** para realizar as seguintes etapas:

### Funcionalidades

1. **Entrada do Usuário**:
   - O usuário insere uma data no formato `YYYY-MM-DD` para escolher o ano desejado.

2. **Web Scraping do Billboard Hot 100**:
   - O programa acessa o site da Billboard e extrai os nomes das 100 músicas mais populares na data fornecida.

3. **Integração com o Spotify**:
   - Utilizando a API do Spotify, o programa:
     - Autentica o usuário.
     - Busca as músicas extraídas no Spotify.
     - Cria uma playlist privada no Spotify com as músicas encontradas.

4. **Criação da Playlist**:
   - As músicas encontradas são adicionadas à playlist criada no Spotify.

### Fluxo do Programa

1. O usuário insere uma data válida no formato `YYYY-MM-DD`.
2. O programa valida a data e realiza uma requisição ao site da Billboard para obter as músicas do **Hot 100**.
3. As músicas são buscadas no Spotify, e as que forem encontradas são adicionadas a uma nova playlist privada.
4. Ao final, o programa exibe uma mensagem confirmando a criação da playlist.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **BeautifulSoup**: Para realizar o web scraping e extrair os dados do site da Billboard.
- **Requests**: Para realizar requisições HTTP ao site da Billboard.
- **Spotipy**: Para integração com a API do Spotify e automação da criação de playlists.

## Pré-requisitos

1. **Spotify Developer Account**:
   - Crie um aplicativo no [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) para obter o `CLIENT_ID` e o `CLIENT_SECRET`.

2. **Instalar as Dependências**:
   - Execute o seguinte comando para instalar as bibliotecas necessárias:
     ```bash
     pip install requests beautifulsoup4 spotipy
     ```

3. **Configurar o Ambiente**:
   - Substitua as variáveis `CLIENT_ID` e `CLIENT_SECRET` no código pelos valores obtidos no Spotify Developer Dashboard.

## Como Executar o Projeto

1. Clone ou baixe este repositório.
2. Navegue até o diretório do projeto.
3. Execute o script `main.py`:
   ```bash
   python main.py
   ```
4. Insira uma data no formato `YYYY-MM-DD` quando solicitado.
5. Faça login no Spotify quando o navegador abrir.
6. Aguarde a criação da playlist e confira no seu perfil do Spotify.

## Observações

- Nem todas as músicas do Billboard Hot 100 podem estar disponíveis no Spotify. O programa informará quais músicas foram ignoradas.
- Certifique-se de que o `CLIENT_ID` e o `CLIENT_SECRET` estão corretos para evitar erros de autenticação.

## Exemplo de Uso

1. O programa solicita:
   ```
   Wich year do you want to travel to? Type the date in this format YYYY-MM-DD:
   ```
2. O usuário insere:
   ```
   2000-08-12
   ```
3. O programa cria uma playlist chamada `2000-08-12 Billboard 100` no Spotify com as músicas disponíveis.

## Licença

Este projeto é apenas para fins educacionais e não deve ser usado para fins comerciais.
