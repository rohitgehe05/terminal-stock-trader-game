import view
import create_db

def main():
    create_db.create_tables()
    view.main_menu()

main()
