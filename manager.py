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

def edit_contact(contacts, contact_index, new_name, new_phone, new_email):
    adjusted_index = int(contact_index) - 1
    if adjusted_index >= 0 and adjusted_index < len(contacts):
        contacts[adjusted_index]['name'] = new_name
        contacts[adjusted_index]['phone'] = new_phone
        contacts[adjusted_index]['email'] = new_email
        print('Contato {} atualizado para {}'.format(contact_index, new_name))
    else:
        print('\nÍndice de contato inválido')
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

    elif choice == '3':
        view_contacts(contacts)
        contact_index = input('Digite o número do contato que deseja editar: ')
        new_name = input('Digite o novo nome do contato: ')
        new_phone = input('Digite o novo telefone do contato: ')
        new_email = input('Digite o novo email do contato: ')
        edit_contact(contacts, contact_index, new_name, new_phone, new_email)