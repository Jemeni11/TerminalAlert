import argparse
from pathlib import Path
from os.path import join, dirname, realpath
import subprocess
from notifypy import Notify
import time

notification = Notify(
    default_notification_application_name="TerminalAlert",
    default_notification_icon=join(dirname(realpath(__file__)), 'logo.png')
)


def run_command(cmd: str) -> tuple[int, bytes, bytes, float]:
    start_time = time.time()
    process = subprocess.run(cmd, shell=True, capture_output=True)
    end_time = time.time()
    execution_time = end_time - start_time
    return process.returncode, process.stdout, process.stderr, execution_time


def check_status(return_code: int) -> str:
    return "Success" if return_code == 0 else "Failure"


def send_notification(title: str, message: str) -> None:
    try:
        notification.title = title
        notification.message = message

        failure_icon = Path(join(dirname(realpath(__file__)), 'failure.png'))
        success_icon = Path(join(dirname(realpath(__file__)), 'success.png'))

        icon = success_icon if title == "Success" else failure_icon

        if not icon.exists():
            print(f"Warning: Icon file not found: {icon}")
        else:
            notification.icon = str(icon)

        notification.send()

    except Exception as e:
        print(f"Error sending notification: {e}")


def terminal_alert(cmd: str) -> None:
    return_code, stdout, stderr, execution_time = run_command(cmd)
    status = check_status(return_code)
    message = f"The command '{cmd}' has finished running.\nExecution time: {execution_time:.2f} seconds"
    send_notification(status, message)

    standard_output = stdout.decode().strip() if stdout else None
    standard_error = stderr.decode().strip() if stderr else None

    print(f"Output: {standard_output}")
    print(f"Error: {standard_error}")
    print(f"Execution time: {execution_time:.2f} seconds")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a command and notify on completion.")
    parser.add_argument("command", help="The command to run.")
    args = parser.parse_args()

    terminal_alert(args.command)
