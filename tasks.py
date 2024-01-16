from robocorp.tasks import task
from GnucashLibrary import GnucashLibrary

@task
def create_account():
  lib = GnucashLibrary()

  try:
    lib.open_gnucash()
    lib.open_create_new_account_form()
    lib.fill_data()
    lib.click_cancel()
  finally:
    lib.close_gnucash()
    lib.remove_lock_file()
