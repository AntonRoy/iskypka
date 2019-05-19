def configurate_message(client_name, phone_number, email, model, memory_size, color, state, other_information, to):
    border = "--------------------------------------------"

    client_information = "\n Имя клиента: {0} \n Телефон: {1} \n Email: {2} \n".format(
                                                            client_name, 
                                                            phone_number, 
                                                            email
                                                        )

    phone_information = "\n Модель телефона: {0} \n Память: {1} \n Цвет: {2} \n Состояние: {3} \n Дополнительная информация: {4} \n Ответить: {5} \n".format(
                                                                                                                                    model,
                                                                                                                                    memory_size,
                                                                                                                                    color,
                                                                                                                                    state,
                                                                                                                                    other_information,
                                                                                                                                    to

        )
    email_body = border + client_information + border + phone_information + border
    return email_body