import subprocess

def lambda_handler(event, context):
    from subprocess import check_output,CalledProcessError
    try:
        retcode = subprocess.call("curl -XPOST -H 'Content-Type: application/x-www-form-urlencoded' -H 'X-aws-origin:LAMBDA_NAME' 'http://urlencoded?firstname=sid'", shell=True)
        success = True
    except CalledProcessError as e:
        output = e.output.decode()
        success = False
