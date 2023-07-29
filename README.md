# MVP

손 위생 관리 스마트 미러

### SetUp

- VirtualEnvs

  - use env

  ```
  poetry config virtualenvs.in-project true
  ```

  - env activate & deactivate

  ```
  poetry shell
  exit
  ```

  - library install

  ```
  poetry install
  ```

- Run
  - `main.py`
  ```
  cd api_server && poetry run uvicorn main:app
  ```

### API endpoints

| 요청 |             url              |        설명         |
| :--: | :--------------------------: | :-----------------: |
| GET  | http://127.0.0.1:8000/video/ | 실시간 웹 캠 활성화 |
| GET  | http://127.0.0.1:8000/close/ |   실시간 캠 종료    |
