release: bash ./release.sh
web: gunicorn hyperdrive_backend.wsgi
celery_worker: celery -A hyperdrive_backend worker -Q celery -n celery@%h
celery_worker_pull_token: celery -A hyperdrive_backend worker -Q pull_token -n pull_token@%h
celery_worker_stats: celery -A hyperdrive_backend worker -Q stats -n stats@%h
celery_worker_process_txn: celery -A hyperdrive_backend worker -Q process_txn -n process_txn@%h
celery_worker_process_txn_backfill: celery -A hyperdrive_backend worker -Q process_txn_backfill -n process_txn_backfill@%h
celery_worker_refresh_token: celery -A hyperdrive_backend worker -Q refresh_token -n refresh_token@%h
