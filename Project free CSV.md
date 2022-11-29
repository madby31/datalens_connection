# Проект Свободный CSV
## Цель: Создать архитектуру для удобного бесплатного использования CSV в Yandex DataLens

Предварительная схема

```mermaid
graph TD;
    A[CSV] --> D{Python script};
    B[XLSX] --> D;
    C(Task Scheduler) --> D;
    D --> E[Backup table];
    D ----> F(Yandex Object Storage);
    F --> G(Yandex Query);
    G --> H(Yandex DataLens);
    
```

Материалы:

* [Визуализация данных из Yandex Object Storage на дашбордах Yandex DataLens](https://cloud.yandex.ru/docs/query/tutorials/datalens)
* [Yandex Object Storage](https://cloud.yandex.ru/docs/storage/)
* [Yandex Query](https://cloud.yandex.ru/services/query)
* [Yandex DataLens](https://cloud.yandex.ru/docs/datalens/)

:octocat: По стоимости сервисов Yandex:

[Уровень нетарифицируемого использования (free tier) для сервисов экосистемы бессерверных вычислений](https://cloud.yandex.ru/docs/billing/concepts/serverless-free-tier)

Разсширение:
[Создание таймера, который вызывает функцию Cloud Functions](https://cloud.yandex.ru/docs/functions/operations/trigger/timer-create)
