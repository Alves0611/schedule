def add_contact(contacts, name, phone, email, favorite=False):
    contact = {'name': name, 'phone': phone, 'email': email, 'favorite': favorite}
    contacts.append(contact)
    print('Contato {} foi adicionado com sucesso'.format(name))
    return

def view_contacts(contacts):
    print('\nLista de contatos:')
    for index, contact in enumerate(contacts, start=1):
        favorite_status = '★' if contact['favorite'] else ''
        contact_name = contact['name']
        contact_phone = contact['phone']
        contact_email = contact['email']
        print('{}. {} {} [{}]'.format(index, contact_name, favorite_status, contact_phone, contact_email))
    return

contacts = []

while True:
    print('\nMenu da Agenda:')
    print('1. Adicionar contato')
    print('2. Ver contatos')
    print('3. Editar contato')
    print('4. Marcar/Desmarcar como favorito')
    print('5. Apagar contato')
    print('6. Sair')

    choice = input('Digite a sua escolha: ')


    if choice == '1':
        name = input('Digite o nome do contato: ')
        phone = input('Digite o telefone do contato: ')
        email = input('Digite o email do contato: ')
        favorite = input('Marcar como favorito? (S/N): ').upper() == 'S'
        add_contact(contacts, name, phone, email, favorite)

    elif choice == '2':
        view_contacts(contacts)