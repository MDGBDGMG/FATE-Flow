from .resource import BaseAPI


class Federated(BaseAPI):
    def create_job(self, job_id, roles, command_body):
        return self.job_command(job_id=job_id, roles=roles, command="create", command_body=command_body,
                                parallel=False)

    def stop_job(self, job_id, roles):
        return self.job_command(job_id=job_id, roles=roles, command="stop")

    def sync_job_status(self, job_id, roles, command_body=None):
        return self.job_command(job_id=job_id, roles=roles, command=f"status/update", command_body=command_body)

    def resource_for_job(self, job_id, roles, operation_type):
        return self.job_command(job_id=job_id, roles=roles, command=f"resource/{operation_type}")

    def start_job(self, job_id, roles, command_body=None):
        return self.job_command(job_id=job_id, roles=roles, command="start", command_body=command_body)

    def update_job(self, job_id, roles, command_body=None):
        return self.job_command(job_id=job_id, roles=roles, command="update", command_body=command_body)

    def save_pipelined_model(self, job_id, roles):
        return self.job_command(job_id=job_id, roles=roles, command="pipeline/save")

    def clean_job(self, job_id, roles, command_body=None):
        return self.job_command(job_id=job_id, roles=roles, command="clean", command_body=command_body)

    def resource_for_task(self, tasks, operation_type):
        return self.task_command(tasks=tasks, command=f"resource/{operation_type}")

    def create_task(self, tasks, command_body=None):
        return self.task_command(tasks=tasks, command="create", command_body=command_body)

    def start_task(self, tasks):
        return self.task_command(tasks=tasks, command="start")

    def rerun_task(self, tasks, task_version):
        return self.task_command(tasks=tasks, command="rerun", command_body={"new_version": task_version})

    def collect_task(self, tasks):
        return self.task_command(tasks=tasks, command="collect")

    def sync_task_status(self, tasks, command_body=None):
        return self.task_command(tasks=tasks, command=f"status/update", command_body=command_body)

    def stop_task(self, tasks, command_body=None):
        return self.task_command(tasks=tasks, command="stop", command_body=command_body)

    def clean_task(self, tasks, content_type):
        return self.task_command(tasks=tasks, command="clean/{}".format(content_type))
