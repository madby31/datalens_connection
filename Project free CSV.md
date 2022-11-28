# Проект Свободный CSV
## Цель: Создать архитектуру для удобного бесплатного использования CSV в Yandex DataLens

Предварительная схема

```mermaid
graph TD;
    A[CSV]-->D{Python script};
    B[XLSX]-->D{Python script};
    C(Task Scheduler)-->D{Python script};
    D{Python script}<-->E(Backup table);
    D{Python script}-->F(Yandex Object Storage);
    F(Yandex Object Storage)-->G(Yandex Query);
    G(Yandex Query)-->H(Yandex DataLens);
    
```

Материалы:

* [Визуализация данных из Yandex Object Storage на дашбордах Yandex DataLens](https://cloud.yandex.ru/docs/query/tutorials/datalens)
* [Yandex Object Storage](https://cloud.yandex.ru/docs/storage/)
* [Yandex Query](https://cloud.yandex.ru/services/query)
* [Yandex DataLens](https://cloud.yandex.ru/docs/datalens/)

По стоимости сервисов Yandex:

[Уровень нетарифицируемого использования (free tier) для сервисов экосистемы бессерверных вычислений](https://cloud.yandex.ru/docs/billing/concepts/serverless-free-tier)
