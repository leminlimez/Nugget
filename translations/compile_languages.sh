# macOS only

# use python venv
source ../.env/bin/activate

for i in *.ts; do
    [ -f "$i" ] || break
    fnoext="${i%.*}.qm"
    pyside6-lrelease "$i" "$fnoext"
done