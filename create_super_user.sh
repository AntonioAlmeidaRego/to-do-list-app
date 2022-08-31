#!/bin/bash -x

python manage.py migrate --noinput || exit 1
python manage.py create_super_user antonio.alm1020@gmail.com antonio.alm1020@gmail.com 123 || exit 1
exec "$@"