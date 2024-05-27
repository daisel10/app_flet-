from typing import Union
import flet as ft
from views.Router import Router
from views.matwa import funcs
import datetime

WIDTH = 800 * 9 / 16
HEIGHT = 800 * 16 / 9

def Inventario(router_data: Union[Router, str, None] = None):
    
    container = ft.Container()
    
    page = router_data.page
    
    depositInput = ft.TextField(label="Cantidad a Depositar/Retirar")

    purposeInput = ft.TextField(label="Motivo de Retiro")
    balanceText = ft.Text(
        value=f"Saldo:{funcs.GetBalance()}",
        size=20,
        text_align=ft.TextAlign.CENTER,
        width=WIDTH,
    )

    def onDepositClick(e):
        valueToDeposit = int(depositInput.value)
        funcs.deposit(valueToDeposit, datetime.date.today())
        balanceText.value = f"Saldo:{funcs.GetBalance()}"
        update_operations()
        page.update()

    def onWithdrawClick(e):
        valueToWidthdraw = int(depositInput.value)
        purpose = purposeInput.value
        funcs.withdraw(valueToWidthdraw, purpose, datetime.date.today())
        balanceText.value = f"Saldo:{funcs.GetBalance()}"
        update_operations()
        page.update()

    depositBtn = ft.ElevatedButton(text="Depositar", on_click=onDepositClick)

    withdrawBtn = ft.ElevatedButton(text="Retirar", on_click=onWithdrawClick)

    balance = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    balanceText,
                    depositInput,
                    purposeInput,
                    ft.Row(
                        controls=[
                            depositBtn,
                            withdrawBtn,
                        ],
                        width=WIDTH,
                    ),
                ],
                width=WIDTH,
            ),
            width=WIDTH,
        )
    )

    operations = ft.Column(
        controls=[ft.Text(value=f"{op}") for op in funcs.operations],
        height=HEIGHT / 4,
        scroll=ft.ScrollMode.ALWAYS,
    )

    def update_operations():
        operations.controls = [ft.Text(value=f"{op}") for op in funcs.operations][::-1]

    TransactionHistory = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[ft.Text("Historial de Transacciones:"), operations]
            ),
            padding=10,
            width=WIDTH,
        )
    )
    
    container.content = ft.Column(
        controls=[
            balance,
            TransactionHistory,
        ],

    )
    
    router_data.page.title = "Inventario"
    router_data.page.add(container)
    
    return container 