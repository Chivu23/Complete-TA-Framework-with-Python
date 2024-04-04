import subprocess
if __name__ == '__maine__':
    s = subprocess.run('behave -f html -o reports/smoke.html --tags=smoke', shell=True, check=True)
