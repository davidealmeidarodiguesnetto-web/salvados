import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class ERPGotinhaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ERP Gotinha - Sistema Interativo")
        self.geometry("950x620")

        # Banco de dados em memória (listas dinâmicas)
        self.categorias = [
            {"id": 1, "nome": "Produtos Alimentícios", "status": "Ativo"},
            {"id": 2, "nome": "Serviços Prestados", "status": "Ativo"},
            {"id": 3, "nome": "Insumos e Materiais", "status": "Inativo"}
        ]

        self.pagamentos = [
            {"nome": "PIX", "desc": "À Vista / Instantâneo", "status": "Ativo"},
            {"nome": "Cartão de Crédito", "desc": "Permite Parcelamento", "status": "Ativo"},
            {"nome": "Boleto Bancário", "desc": "Vencimento em 3 dias", "status": "Ativo"}
        ]

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ------------------- SIDEBAR -------------------
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

        self.logo_canvas = ctk.CTkCanvas(self.sidebar_frame, width=50, height=50, bg="#2b2b2b", highlightthickness=0)
        self.logo_canvas.grid(row=0, column=0, pady=(20, 5), padx=10)
        self.desenhar_logo_gotinha()

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="ERP GOTINHA", font=ctk.CTkFont(size=18, weight="bold"), text_color="#38bdf8")
        self.logo_label.grid(row=1, column=0, padx=20, pady=(0, 20))

        self.btn_dash = ctk.CTkButton(self.sidebar_frame, text="Dashboard", command=self.mostrar_dashboard)
        self.btn_dash.grid(row=2, column=0, padx=20, pady=8, sticky="ew")

        self.btn_categorias = ctk.CTkButton(self.sidebar_frame, text="Categorias", fg_color="transparent", text_color="#94a3b8", command=self.mostrar_categorias)
        self.btn_categorias.grid(row=3, column=0, padx=20, pady=8, sticky="ew")

        self.btn_pagamentos = ctk.CTkButton(self.sidebar_frame, text="Forma de Pagamento", fg_color="transparent", text_color="#94a3b8", command=self.mostrar_pagamentos)
        self.btn_pagamentos.grid(row=4, column=0, padx=20, pady=8, sticky="ew")

        # ------------------- ÁREA PRINCIPAL -------------------
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.mostrar_dashboard()

    def reset_botoes(self):
        self.btn_dash.configure(fg_color="transparent", text_color="#94a3b8")
        self.btn_categorias.configure(fg_color="transparent", text_color="#94a3b8")
        self.btn_pagamentos.configure(fg_color="transparent", text_color="#94a3b8")

    def limpar_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # ------------------- DASHBOARD -------------------
    def mostrar_dashboard(self):
        self.limpar_main_frame()
        self.reset_botoes()
        self.btn_dash.configure(fg_color="#0284c7", text_color="#ffffff")

        ctk.CTkLabel(self.main_frame, text="Painel de Gestão", font=ctk.CTkFont(size=22, weight="bold")).pack(anchor="w", pady=(0, 20))

        cards_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        cards_frame.pack(fill="x", pady=(0, 20))

        # Indicadores calculados dinamicamente
        self.criar_card(cards_frame, "Categorias", str(len(self.categorias)), 0)
        self.criar_card(cards_frame, "Formas de Pagamento", str(len(self.pagamentos)), 1)
        self.criar_card(cards_frame, "Vendas Hoje", "R$ 1.450,00", 2)
        self.criar_card(cards_frame, "Status do Sistema", "Online", 3)

        table_frame = ctk.CTkScrollableFrame(self.main_frame, height=300)
        table_frame.pack(fill="both", expand=True)

        ctk.CTkLabel(table_frame, text="Resumo de Atividades Recentes", font=ctk.CTkFont(size=16, weight="bold")).pack(anchor="w", padx=15, pady=10)

        for cat in self.categorias:
            row = ctk.CTkFrame(table_frame, fg_color="#1e293b")
            row.pack(fill="x", padx=10, pady=4)
            ctk.CTkLabel(row, text=f"Categoria: {cat['nome']}", anchor="w").pack(side="left", padx=15, pady=8)
            ctk.CTkLabel(row, text=f"Status: {cat['status']}", text_color="#38bdf8").pack(side="right", padx=15)

    # ------------------- CATEGORIAS (CADASTRO + EXCLUSÃO) -------------------
    def mostrar_categorias(self):
        self.limpar_main_frame()
        self.reset_botoes()
        self.btn_categorias.configure(fg_color="#0284c7", text_color="#ffffff")

        ctk.CTkLabel(self.main_frame, text="Gestão de Categorias", font=ctk.CTkFont(size=22, weight="bold")).pack(anchor="w", pady=(0, 15))

        # Formulário
        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.pack(fill="x", pady=(0, 15))

        ctk.CTkLabel(form_frame, text="Nome:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=10, pady=12)
        self.input_cat_nome = ctk.CTkEntry(form_frame, placeholder_text="Digite o nome...", width=250)
        self.input_cat_nome.pack(side="left", padx=10, pady=12)

        self.input_cat_status = ctk.CTkOptionMenu(form_frame, values=["Ativo", "Inativo"], width=100)
        self.input_cat_status.pack(side="left", padx=10, pady=12)

        btn_add = ctk.CTkButton(form_frame, text="Adicionar", fg_color="#15803d", width=100, command=self.adicionar_categoria)
        btn_add.pack(side="left", padx=10, pady=12)

        self.lbl_cat_msg = ctk.CTkLabel(self.main_frame, text="", text_color="#ef4444")
        self.lbl_cat_msg.pack(anchor="w", pady=(0, 5))

        # Listagem Rolável
        self.cat_list_frame = ctk.CTkScrollableFrame(self.main_frame)
        self.cat_list_frame.pack(fill="both", expand=True)

        self.atualizar_lista_categorias()

    def adicionar_categoria(self):
        nome = self.input_cat_nome.get().strip()
        status = self.input_cat_status.get()

        if not nome:
            self.lbl_cat_msg.configure(text="Erro: O nome da categoria não pode ser vazio!")
            return

        novo_id = max([c["id"] for c in self.categorias], default=0) + 1
        self.categorias.append({"id": novo_id, "nome": nome, "status": status})
        self.input_cat_nome.delete(0, "end")
        self.lbl_cat_msg.configure(text="")
        self.atualizar_lista_categorias()

    def remover_categoria(self, cat_id):
        self.categorias = [c for c in self.categorias if c["id"] != cat_id]
        self.atualizar_lista_categorias()

    def atualizar_lista_categorias(self):
        for w in self.cat_list_frame.winfo_children():
            w.destroy()

        for cat in self.categorias:
            row = ctk.CTkFrame(self.cat_list_frame, fg_color="#1e293b")
            row.pack(fill="x", padx=5, pady=4)

            ctk.CTkLabel(row, text=f"ID: {cat['id']}", width=50).pack(side="left", padx=10)
            ctk.CTkLabel(row, text=cat['nome'], anchor="w").pack(side="left", fill="x", expand=True, padx=10)
            
            color = "#15803d" if cat['status'] == "Ativo" else "#a16207"
            ctk.CTkLabel(row, text=cat['status'], text_color=color, width=80).pack(side="left", padx=10)

            btn_del = ctk.CTkButton(row, text="Excluir", fg_color="#b91c1c", hover_color="#991b1b", width=70, height=24,
                                    command=lambda c_id=cat['id']: self.remover_categoria(c_id))
            btn_del.pack(side="right", padx=10, pady=5)

    # ------------------- FORMAS DE PAGAMENTO -------------------
    def mostrar_pagamentos(self):
        self.limpar_main_frame()
        self.reset_botoes()
        self.btn_pagamentos.configure(fg_color="#0284c7", text_color="#ffffff")

        ctk.CTkLabel(self.main_frame, text="Formas de Pagamento", font=ctk.CTkFont(size=22, weight="bold")).pack(anchor="w", pady=(0, 15))

        # Form
        form_frame = ctk.CTkFrame(self.main_frame)
        form_frame.pack(fill="x", pady=(0, 15))

        self.input_pag_nome = ctk.CTkEntry(form_frame, placeholder_text="Nome (ex: PIX)", width=180)
        self.input_pag_nome.pack(side="left", padx=8, pady=12)

        self.input_pag_desc = ctk.CTkEntry(form_frame, placeholder_text="Descrição/Detalhes", width=240)
        self.input_pag_desc.pack(side="left", padx=8, pady=12)

        btn_add = ctk.CTkButton(form_frame, text="Cadastrar", fg_color="#15803d", width=100, command=self.adicionar_pagamento)
        btn_add.pack(side="left", padx=8, pady=12)

        self.lbl_pag_msg = ctk.CTkLabel(self.main_frame, text="", text_color="#ef4444")
        self.lbl_pag_msg.pack(anchor="w", pady=(0, 5))

        self.pag_list_frame = ctk.CTkScrollableFrame(self.main_frame)
        self.pag_list_frame.pack(fill="both", expand=True)

        self.atualizar_lista_pagamentos()

    def adicionar_pagamento(self):
        nome = self.input_pag_nome.get().strip()
        desc = self.input_pag_desc.get().strip()

        if not nome or not desc:
            self.lbl_pag_msg.configure(text="Erro: Preencha todos os campos do pagamento!")
            return

        self.pagamentos.append({"nome": nome, "desc": desc, "status": "Ativo"})
        self.input_pag_nome.delete(0, "end")
        self.input_pag_desc.delete(0, "end")
        self.lbl_pag_msg.configure(text="")
        self.atualizar_lista_pagamentos()

    def remover_pagamento(self, nome):
        self.pagamentos = [p for p in self.pagamentos if p["nome"] != nome]
        self.atualizar_lista_pagamentos()

    def atualizar_lista_pagamentos(self):
        for w in self.pag_list_frame.winfo_children():
            w.destroy()

        for pag in self.pagamentos:
            row = ctk.CTkFrame(self.pag_list_frame, fg_color="#1e293b")
            row.pack(fill="x", padx=5, pady=4)

            ctk.CTkLabel(row, text=pag['nome'], font=ctk.CTkFont(weight="bold"), width=150, anchor="w").pack(side="left", padx=10)
            ctk.CTkLabel(row, text=pag['desc'], anchor="w").pack(side="left", fill="x", expand=True, padx=10)

            btn_del = ctk.CTkButton(row, text="Excluir", fg_color="#b91c1c", hover_color="#991b1b", width=70, height=24,
                                    command=lambda p_nome=pag['nome']: self.remover_pagamento(p_nome))
            btn_del.pack(side="right", padx=10, pady=5)

    def desenhar_logo_gotinha(self):
        self.logo_canvas.create_polygon(25, 5, 42, 32, 35, 45, 15, 45, 8, 32, fill="#38bdf8", outline="")
        self.logo_canvas.create_oval(18, 22, 26, 32, fill="#7dd3fc", outline="")

    def criar_card(self, parent, titulo, valor, coluna):
        card = ctk.CTkFrame(parent)
        card.grid(row=0, column=coluna, padx=5, sticky="ew")
        parent.grid_columnconfigure(coluna, weight=1)

        ctk.CTkLabel(card, text=titulo, font=ctk.CTkFont(size=12), text_color="#94a3b8").pack(anchor="w", padx=15, pady=(10, 0))
        ctk.CTkLabel(card, text=valor, font=ctk.CTkFont(size=18, weight="bold")).pack(anchor="w", padx=15, pady=(0, 10))

if __name__ == "__main__":
    app = ERPGotinhaApp()
    app.mainloop()