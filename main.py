from tokenize import String
from unicodedata import decimal
from xml.sax import parseString
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex, rgba
from kivymd.app import MDApp
from kivy.properties import BooleanProperty, StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
import mysql.connector
from kivy.core.window import Window
import cryptocode
from kivy.clock import Clock
from kivymd.uix.snackbar import Snackbar
from kivy.metrics import dp
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem
import pyperclip


Window.size = (1200, 700)
#query para receber o cargo por escrito do devido trabalhador -> "SELECT Cargos.Cargo From Cargos,Trabalhadores WHERE Cargos.Permissao=Trabalhadores.Cargo AND Trabalhadores.Nome='João Aleixo'"

class WindowManager(ScreenManager):
    pass




class Login(Screen, object):
    username = ""
    def __init__(self, **kw):
        super().__init__(**kw)

    def validate_login(self):
        wm = MDApp.get_running_app().root
        try:
            self.mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
            self.mycursor = self.mydb.cursor()
            print("ta nice222")
        except Exception as a:
            wm.current = "ServersDown"
        #utilizador
        try:
            self.query_user = "SELECT ID From trabalhadores WHERE ID='" + self.ids.text_field_user.text + "'"
            self.mycursor.execute(self.query_user)
            self.myresult = self.mycursor.fetchone()
            for Login.username in self.myresult: #devolve o valor do campo formatado (apenas o numero)
                print(Login.username)
            self.mydb.commit()

            #palavra-passe
            
            self.query_pass = "SELECT Password From trabalhadores WHERE ID='" + self.ids.text_field_user.text + "'"
            self.mycursor.execute(self.query_pass)
            self.myresult = self.mycursor.fetchone()
            for self.password in self.myresult:
                print(self.password)
            self.mydb.commit()
            print(cryptocode.decrypt(self.password, "wow"))
            if self.ids.text_field_pass.text == cryptocode.decrypt(self.password, "wow"):
                print("teste1 passado")
                self.query_perms = "SELECT Cargo From trabalhadores WHERE id='" + self.ids.text_field_user.text + "'"
                self.mycursor.execute(self.query_perms)
                self.myresult = self.mycursor.fetchone()
                for self.permissao in self.myresult: #devolve o valor do campo formatado (apenas o numero)
                    print(self.permissao)
                    self.query_matchid = "SELECT Nome From trabalhadores WHERE id='" + self.ids.text_field_user.text + "'"    
                    self.mycursor.execute(self.query_matchid)
                    self.myresult = self.mycursor.fetchone()
                    for self.nameid in self.myresult:
                        pass
                    


                    try:
                        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
                        mycursor = mydb.cursor()
                    except Exception as e:
                        wm.current = "ServersDown"
                    query_state = "SELECT Estado From trabalhadores WHERE ID='" + self.ids.text_field_user.text + "'"
                    mycursor.execute(query_state)
                    myresult = mycursor.fetchone()
                    for estado in myresult:
                        pass
                    print(estado)
                    mydb.commit()

                    self.ids.text_field_user.text = ""
                    self.ids.text_field_pass.text = ""

                    if estado == "Ativo":
                        if self.permissao == 0: #gerente
                            self.snack_show(self.nameid, "Gerente")
                            wm.current = "DashboardGerente"
                            self.cargo = "Gerente"
                            DashboardGerente.profile_maker(self)
                            MDApp.get_running_app().provider_opacity = 1
                            MDApp.get_running_app().provider_disable_box = False
                            MDApp.get_running_app().provider_menu = False
                            MDApp.get_running_app().produtos_menu = False
                            MDApp.get_running_app().empregados_menu = False
                            MDApp.get_running_app().empregados_disabled = False
                            MDApp.get_running_app().empregados_opacity = 1
                            MDApp.get_running_app().seccoes_menu = False

                            
                        elif self.permissao == 1: #chefe de loja
                            self.snack_show(self.nameid, "Chefe de Loja")
                            self.cargo = "Chefe de Loja"
                            wm.current = "DashboardGerente"
                            DashboardGerente.profile_maker(self)
                            MDApp.get_running_app().provider_opacity = 1
                            MDApp.get_running_app().provider_disable_box = False
                            MDApp.get_running_app().provider_menu = False
                            MDApp.get_running_app().produtos_menu = False
                            MDApp.get_running_app().empregados_menu = False
                            MDApp.get_running_app().empregados_disabled = False
                            MDApp.get_running_app().empregados_opacity = 1
                            MDApp.get_running_app().seccoes_menu = False

                        elif self.permissao == 2: #Chefe de seção
                            self.snack_show(self.nameid, "Chefe de Secção") #-------------------
                            self.cargo = "Chefe de Secção"
                            wm.current = "DashboardGerente"
                            DashboardGerente.profile_maker(self)
                            MDApp.get_running_app().provider_opacity = 0
                            MDApp.get_running_app().provider_disable_box = True
                            MDApp.get_running_app().provider_menu = True
                            MDApp.get_running_app().produtos_menu = False
                            MDApp.get_running_app().empregados_menu = False
                            MDApp.get_running_app().empregados_disabled = False
                            MDApp.get_running_app().empregados_opacity = 1
                            MDApp.get_running_app().seccoes_menu = True
                            
                        elif self.permissao == 3: #Funcionário
                            self.snack_show(self.nameid, "Funcionário")
                            self.cargo = "Funcionário"
                            wm.current = "DashboardGerente"
                            DashboardGerente.profile_maker(self)
                            MDApp.get_running_app().provider_opacity = 0
                            MDApp.get_running_app().provider_disable_box = True
                            MDApp.get_running_app().provider_menu = True
                            MDApp.get_running_app().produtos_menu = False
                            MDApp.get_running_app().empregados_menu = True
                            MDApp.get_running_app().empregados_disabled = True
                            MDApp.get_running_app().empregados_opacity = 0
                            MDApp.get_running_app().seccoes_menu = True
                            
                        elif self.permissao == 4: #estagiário
                            self.snack_show(self.nameid, "Estagiário")
                            self.cargo = "Estagiário"
                            wm.current = "DashboardGerente"
                            DashboardGerente.profile_maker(self)
                            MDApp.get_running_app().provider_opacity = 0
                            MDApp.get_running_app().provider_disable_box = True
                            MDApp.get_running_app().provider_menu = True
                            MDApp.get_running_app().produtos_menu = True
                            MDApp.get_running_app().empregados_menu = True
                            MDApp.get_running_app().empregados_disabled = True
                            MDApp.get_running_app().empregados_opacity = 0
                            MDApp.get_running_app().seccoes_menu = True

                    else: 
                        Snackbar(text="A sua conta está desativada!",duration = 1,snackbar_x="10dp", snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5}).open()
            else:
                Snackbar(text="Nome de utilizador ou palavra-passe errado!",duration = 1,snackbar_x="10dp", snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5}).open()

        except Exception as c:
            print(c)
            Snackbar(text="Nome de utilizador ou palavra-passe errado!",duration = 1,snackbar_x="10dp", snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()

            

    def show_pass(self,widget):
        if widget.state == "normal":
            self.ids.text_field_pass.password = True
        else:
            self.ids.text_field_pass.password = False

    def snack_show(self, username, cargo):
        Snackbar(text="Login realizado com sucesso " + username + " (" + cargo + ")!",duration = 1,snackbar_x="10dp", snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#00ad11"), pos_hint={"center_x":.5}).open()




class Content_encomendas_info(BoxLayout):
    pass





class Content_produtos_info(BoxLayout):
    pass

class Content_produtos_search(BoxLayout):
    def limpar_box(self):
        self.ids.produtos_name_search.text = ""

    def limpar_later(self):
        if MDApp.get_running_app().search_produtos_ok == True:
            self.ids.produtos_name_search.text = ""
            MDApp.get_running_app().search_produtos_ok = False


class Content_produtos_remove(BoxLayout):
    def limpar_box(self):
        self.ids.produtos_name_remove.text = ""

    def limpar_later(self):
        if MDApp.get_running_app().remove_produtos_ok == True:
            self.ids.produtos_name_remove.text = ""
            MDApp.get_running_app().remove_produtos_ok = False


class Content_produtos(BoxLayout):
    def limpar_cols1(self):
        self.ids.nome_produtos.text = ""
        self.ids.id_produtos.text = ""
        self.ids.seccao_produtos.text = ""
        self.ids.preco_produtos.text = ""
        self.ids.stock_produtos.text = ""
        self.ids.fornecedor_produtos.text = ""
        self.ids.desc_produtos.text = ""


    def limpar_cols(self):
        print(MDApp.get_running_app().add_produtos_ok)
        Clock.schedule_once(lambda _: self.limpar_later(), 1)
        
    def limpar_later(self):
        if MDApp.get_running_app().add_produtos_ok == True:
            self.ids.nome_produtos.text = ""
            self.ids.id_produtos.text = ""
            self.ids.seccao_produtos.text = ""
            self.ids.preco_produtos.text = ""
            self.ids.stock_produtos.text = ""
            self.ids.fornecedor_produtos.text = ""
            self.ids.desc_produtos.text = ""

            MDApp.get_running_app().add_produtos_ok = False



















class Content_empregados_info(BoxLayout):
    pass

class Content_empregados_search(BoxLayout):
    def limpar_box(self):
        self.ids.empregados_name_search.text = ""

    def limpar_later(self):
        if MDApp.get_running_app().search_empregados_ok == True:
            MDApp.get_running_app().remove_empregados_ok = False


class Content_empregados_remove(BoxLayout):
    def limpar_box(self):
        self.ids.empregados_name_remove.text = ""

    def limpar_later(self):
        if MDApp.get_running_app().remove_empregados_ok == True:
            self.ids.empregados_name_remove.text = ""
            MDApp.get_running_app().remove_empregados_ok = False


class Content_empregados(BoxLayout):
    def limpar_cols1(self):
        self.ids.empregados_name.text = ""
        self.ids.cargo_empregados.text = ""
        self.ids.password_empregados.text = ""
        self.ids.estado_empregados.text = ""
        self.ids.salario_empregados.text = ""
        self.ids.seccao_empregados.text = ""


    def limpar_cols(self):
        print(MDApp.get_running_app().add_empregados_ok)
        Clock.schedule_once(lambda _: self.limpar_later(), 1)
        
    def limpar_later(self):
        if MDApp.get_running_app().add_empregados_ok == True:
            self.ids.empregados_name.text = ""
            self.ids.cargo_empregados.text = ""
            self.ids.password_empregados.text = ""
            self.ids.estado_empregados.text = ""
            self.ids.salario_empregados.text = ""
            self.ids.seccao_empregados.text = ""

            MDApp.get_running_app().add_empregados_ok = False





















class Content_seccao_info(BoxLayout):
    pass

class Content_seccao_search(BoxLayout):
    def limpar_box(self):
        self.ids.seccao_name_search.text = ""

    def limpar_later(self):
        if MDApp.get_running_app().search_seccao_ok == True:
            MDApp.get_running_app().remove_seccao_ok = False


class Content_seccao_remove(BoxLayout):
    def limpar_box(self):
        self.ids.seccao_name_remove.text = ""

    def limpar_later(self):
        if MDApp.get_running_app().remove_seccao_ok == True:
            self.ids.seccao_name_remove.text = ""
            MDApp.get_running_app().remove_seccao_ok = False


class Content_seccao(BoxLayout):
    def limpar_cols1(self):
        self.ids.seccao_name.text = ""
        self.ids.seccao_id_responsavel.text = ""


    def limpar_cols(self):
        print(MDApp.get_running_app().add_seccao_ok)
        Clock.schedule_once(lambda _: self.limpar_later(), 1)
        
    def limpar_later(self):
        if MDApp.get_running_app().add_seccao_ok == True:
            self.ids.seccao_name.text = ""
            self.ids.seccao_id_responsavel.text = ""

            MDApp.get_running_app().add_seccao_ok = False






















class Content_providers_info(BoxLayout):
    pass

class Content_providers_search(BoxLayout):
    def limpar_box(self):
        self.ids.provider_name_search.text = ""

    def limpar_later(self):
        if MDApp.get_running_app().search_provider_ok == True:
            MDApp.get_running_app().remove_provider_ok = False


class Content_providers_remove(BoxLayout):
    def limpar_box(self):
        self.ids.provider_name_remove.text = ""

    def limpar_later(self):
        if MDApp.get_running_app().remove_provider_ok == True:
            self.ids.provider_name.text = ""
            self.ids.provider_address.text = ""
            self.ids.provider_iban.text = ""
            self.ids.provider_nif.text = ""
            self.ids.provider_telefone.text = ""
            self.ids.provider_email.text = ""
            MDApp.get_running_app().remove_provider_ok = False


class Content_providers(BoxLayout):
    def limpar_cols1(self):
        self.ids.provider_name.text = ""
        self.ids.provider_address.text = ""
        self.ids.provider_iban.text = ""
        self.ids.provider_nif.text = ""
        self.ids.provider_telefone.text = ""
        self.ids.provider_email.text = ""

    def limpar_cols(self):
        print(MDApp.get_running_app().add_provider_ok)
        Clock.schedule_once(lambda _: self.limpar_later(), 1)
        
    def limpar_later(self):
        if MDApp.get_running_app().add_provider_ok == True:
            self.ids.provider_name.text = ""
            self.ids.provider_address.text = ""
            self.ids.provider_iban.text = ""
            self.ids.provider_nif.text = ""
            self.ids.provider_telefone.text = ""
            self.ids.provider_email.text = ""
            MDApp.get_running_app().add_provider_ok = False




class Content(BoxLayout):
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
        mycursor = mydb.cursor()
    except Exception as e:
        print(e)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def clean(self):
        self.ids.new_pass.text = ""
        self.ids.old_pass.text = ""

    def show_passnew(self,widget):
        if widget.state == "normal":
            self.ids.new_pass.password = True
        else:
            self.ids.new_pass.password = False
    def show_passold(self,widget):
        if widget.state == "normal":
            self.ids.old_pass.password = True
        else:
            self.ids.old_pass.password = False
            
    def limpar_passes(self):
        self.ids.old_pass.text = ""
        self.ids.new_pass.text = ""

    def alterar_pass(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
        mycursor = mydb.cursor()
        if self.ids.old_pass.text != "" and self.ids.new_pass.text != "":
            query_getpass = "SELECT password from trabalhadores WHERE id=" + str(Login.username)
            pass_antiga = MDApp.get_running_app().pass_old_change
            mycursor.execute(query_getpass)
            myresult = mycursor.fetchone()
            mydb.commit()
            
            for password in myresult: #devolve o valor do campo formatado (apenas o numero)
                password_old = password
                
                
                if pass_antiga == cryptocode.decrypt(password_old, "wow"):
                    pass_nova = MDApp.get_running_app().pass_new_change
                    pass_nova_cod = cryptocode.encrypt(pass_nova, "wow")

                    query_changepass = "UPDATE trabalhadores SET password='" + pass_nova_cod + "' WHERE id='" + str(Login.username) + "'"
                    mycursor.execute(query_changepass)
                    myresult = mycursor.fetchone()
                    mydb.commit()
                    Snackbar(text="Palavra-passe alterada com sucesso, pode fechar a janela!",duration = 1,snackbar_x="10dp", snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#00ad11"), pos_hint={"center_x":.5}).open()
                    self.ids.old_pass.text = ""
                    self.ids.new_pass.text = ""

                else: 
                    Snackbar(text="A palavra-passe está errada!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()
        else: 
            Snackbar(text="Os campos devem ser preenchidos!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()


class DashboardGerente(Screen):
    def close_menus(self):
        self.ids.menu_providers.close_stack()
        self.ids.menu_produtos.close_stack()
        self.ids.menu_seccao.close_stack()
        self.ids.menu_empregados.close_stack()

        
    def root_app(self):
        wm = MDApp.get_running_app().root
        return wm
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
        mycursor = mydb.cursor()
    except Exception as e:
        wm = root_app
        wm.current = "ServersDown"
    cleaner = 0

    def __init__(self, **kw):
        super().__init__(**kw)

####################################### Perfil #######################################

    dialog = None
    
    nome_utilizador = StringProperty("")
    cargo_utilizador = StringProperty("")
    salario_utilizador = StringProperty("")
    id_utilizador = StringProperty()
    ## ---- recolher dados para informação do perfil do utilizado ---- ##

    def profile_maker(self):
        MDApp.get_running_app().menu_seccao = 1
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
        mycursor = mydb.cursor()
        try:
            print("profile maker")
            query_getprofile = "SELECT Nome, Cargo, Salario, `Secção` from trabalhadores WHERE id=" + str(Login.username)
            mycursor.execute(query_getprofile)
            myresult = mycursor.fetchall()
            for data in myresult:
                print(data[0])
            mydb.commit()
            self.id_utilizador = str(Login.username)
            print("utilizador self data- " + str(self.id_utilizador))
            self.nome_utilizador = str(data[0])
            
            if data[1] == 0:
                self.cargo_utilizador = "Gerente"
                self.perm = 0
            if data[1] == 1:
                self.cargo_utilizador = "Chefe de loja"
                self.perm = 1
            if data[1] == 2:
                self.cargo_utilizador = "Chefe de Secção"
                self.perm = 2
                MDApp.get_running_app().menu_seccao = 0
            if data[1] == 3:
                self.cargo_utilizador = "Funcionário"
                self.perm = 3
            if data[1] == 4:
                self.cargo_utilizador = "Estagiário"
                self.perm = 4

            self.salario_utilizador = str(data[2]) + "€"
            self.seccao_utilizador = data[3]

        except Exception as k:
            print(k)


    ## ---- fim da recolha dos dados ---- ##

    ## ---- Botão de logout do perfil ---- ##
    def Logout(self):
        wm = MDApp.get_running_app().root
        wm.current = "Login"
        self.nome_utilizador = ""
        self.cargo_utilizador = ""
        self.salario_utilizador = ""
        self.id_utilizador = ""
    
    ## ---- Fim botão de logout do perfil ---- ##
    
    def show_alert_dialog(self, obj):
        if not self.dialog:
            
            close_btn = MDFlatButton(text="        ", on_release=self.close_dialog)
            alter_btn = MDFlatButton(text="       ", size_hint=(None,None), size= (100,100))
        
            self.dialog = MDDialog(
                title = "Alterar palavra-passe",
                text = "Preencha os campos",
                content_cls=Content(),
                type="custom",
                buttons=[
                    close_btn,
                    alter_btn,
                ]
            )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


    ####################################### fornecedores fornecedores #######################################

    ## ---- Mostrar conteudo da tabela na scrollview ---- ##

    def make_providers_list(self):

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
        mycursor = mydb.cursor()
        
        sql_select_Query = "select * from fornecedores"
        mycursor.execute(sql_select_Query)
        
        records = mycursor.fetchall()
        print("Total number of rows in table providers: ", mycursor.rowcount)
        row_nr = mycursor.rowcount
        mydb.commit()
        print("\nPrinting each row")
        for row in records:
            try:
                for x in range(6):
                    self.ids["provider_data"].add_widget(
                        OneLineListItem(
                            text=str(row[x]),
                            on_release=self.mais_info
                            )
                        )

            except Exception as b:
                print(b)
 
    dialog_info = None
    ####################### + que da informações sobre o fornecedor 
    def mais_info(self, obj):
        self.titulo = ""
        self.titulo = obj.text
        try: 
            self.dialog_info = None
            if not self.dialog_info:
                ok_btn = MDRaisedButton(text="Ok", on_release=self.close_dialog_provider_info)
                copy_btn = MDRaisedButton(text="Copiar", on_release=self.copy_dialog_info)
                print(self.titulo)
                self.dialog_info = MDDialog(
                    title = self.titulo,
                    content_cls = Content_providers_info(),
                    type="custom",
                    buttons=[
                        copy_btn,
                        ok_btn,
                    ],
                )
            self.dialog_info.open()
            


        except Exception as erro_info:
            print(erro_info)


    def copy_dialog_info(self,obj):
        try: 
            pyperclip.copy(self.titulo)
            self.dialog_info.dismiss()
        except Exception as e:
            print(e)
            Snackbar(text="Parece que esta função não se encontra disponível no seu sistema operativo!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()


    def close_dialog_provider_info(self,obj):
        self.dialog_info.dismiss()

    ############### limpa a lista de fornecedores ###################

    def remove_providers_list(self):
        print("removido")
        self.ids["provider_data"].clear_widgets()


        ###### botoes flutuantes das opcoes ######

    spin = BooleanProperty(False)
    def spinner(self):
        self.spin = False
    def callback_options_provider(self, instance):
        if self.perm == 1 or self.perm == 0:
            if instance.icon == 'refresh':
                self.spin = True
                Clock.schedule_once(lambda _: self.spinner(), 3)
                self.remove_providers_list()
                self.make_providers_list()
            if instance.icon == "pencil-plus-outline":
                self.show_providers(self)
            if instance.icon == "pencil-minus-outline":
                self.show_providers_remove(self)
            if instance.icon == "selection-search":
                self.show_providers_search(self)

    #++++++++++++++++++++++++++ dialog box adicionar fornecedores ++++++++++++++++++++++++++


    dialog_providers = None
    dialog_providers_remove = None
    dialog_providers_search = None


    def close_dialog_provider(self,obj):
        self.dialog_providers.dismiss()

    def show_providers(self, obj):
        if not self.dialog_providers:
            close_btn = MDRaisedButton(text="Cancelar", on_release=self.close_dialog_provider)
            alter_btn = MDRaisedButton(text="Adicionar", on_release=self.add_providers, size_hint=(None,None), size= (100,100))

            self.dialog_providers = MDDialog(
                title = "Adicionar um Fornecedor\n",
                content_cls = Content_providers(),
                type="custom",
                buttons=[
                    close_btn,
                    alter_btn
                ],
            )
        self.dialog_providers.open()

    def add_providers(self, obj):
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
            mycursor = mydb.cursor()
        
            nome = MDApp.get_running_app().provider_nome
            morada = MDApp.get_running_app().provider_morada
            iban = MDApp.get_running_app().provider_iban
            nif = MDApp.get_running_app().provider_nif
            telefone = MDApp.get_running_app().provider_telefone
            email = MDApp.get_running_app().provider_email

            sql_query_add = "INSERT INTO `fornecedores`(`Nome`, `Morada`, `IBAN`, `NIF`, `Nº de telefone`, `Email`) VALUES ('" + nome + "','" + morada + "','" + iban + "','" + nif + "','" + telefone + "','" + email + "')"
            mycursor.execute(sql_query_add)
            mydb.commit()
            Snackbar(text="Fornecedor inserido com sucesso!",duration = 1,snackbar_x="10dp", snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#00ad11"), pos_hint={"center_x":.5}).open()
            self.close_dialog_provider(self)
            self.remove_providers_list()
            self.make_providers_list()
            MDApp.get_running_app().add_provider_ok = True
        except Exception as erro_add:
            if "concatenate" in str(erro_add):
                Snackbar(text="Os campos devem ser preenchidos!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()
            if "1062 (23000)" in str(erro_add):
                Snackbar(text="Já existe um fornecedor com esse nome!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()
    
    #-------------------------- dialog box remover fornecedores --------------------------


    def close_dialog_provider_remove(self,obj):
        self.dialog_providers_remove.dismiss()

    def show_providers_remove(self, obj):
        if not self.dialog_providers_remove:
            close_btn = MDRaisedButton(text="Cancelar", on_release=self.close_dialog_provider_remove)
            alter_btn = MDRaisedButton(text="Remover", on_release=self.remove_providers, size_hint=(None,None), size= (100,100))

            self.dialog_providers_remove = MDDialog(
                title = "Remover um Fornecedor",
                content_cls = Content_providers_remove(),
                type="custom",
                buttons=[
                    close_btn,
                    alter_btn
                ],
            )
        self.dialog_providers_remove.open()


    def remove_providers(self, obj):
        try:
            print(MDApp.get_running_app().remover_nome)
            query_remover = "DELETE FROM fornecedores WHERE Nome='" + MDApp.get_running_app().remover_nome + "'"
            print(query_remover)
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
            mycursor = mydb.cursor()
            mycursor.execute(query_remover)
            mydb.commit()
            MDApp.get_running_app().add_provider_ok = True
            self.close_dialog_provider_remove(obj)
            self.remove_providers_list()
            self.make_providers_list()
            Snackbar(text="Fornecedor apagado com sucesso!",duration = 1,snackbar_x="10dp", snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#00ad11"), pos_hint={"center_x":.5}).open()
        except Exception as e:
            print(e)
            Snackbar(text="Não existe nenhum fornecedor com esse nome!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()

    #??????????????????????????????? dialog box filtrar fornecedores ????????????????????????????????????

    def close_dialog_provider_search(self,obj):
        self.dialog_providers_search.dismiss()

    def show_providers_search(self, obj):
        self.remove_providers_list()
        self.make_providers_list()
        if not self.dialog_providers_search:
            close_btn = MDRaisedButton(text="Cancelar", on_release=self.close_dialog_provider_search)
            alter_btn = MDRaisedButton(text="Procurar", on_release=self.search_providers, size_hint=(None,None), size= (100,100))

            self.dialog_providers_search = MDDialog(
                title = "Pesquisar um Fornecedor",
                content_cls = Content_providers_search(),
                type="custom",
                buttons=[
                    close_btn,
                    alter_btn
                ],
            )
        self.dialog_providers_search.open()

    def search_providers(self, obj):

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
        mycursor = mydb.cursor()
        sql_search_Query = "SELECT * FROM `fornecedores` WHERE Nome REGEXP '" + MDApp.get_running_app().search_nome + "'"
        mycursor.execute(sql_search_Query)
        records = mycursor.fetchall()
        print("Total number of rows in table: ", mycursor.rowcount)
        mydb.commit()
        self.remove_providers_list()
        print("\nPrinting each row")
        self.close_dialog_provider_search(self)
        for row in records:
            try:
                for x in range(6):
                    self.ids["provider_data"].add_widget(
                        OneLineListItem(
                            text=str(row[x]),
                            on_release=self.mais_info
                            )
                        )
                
            except Exception as b:
                print(b)
                self.close_dialog_provider_search(self)


























####################################### aba seccoes ###############################

    def make_seccao_list(self):
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
        mycursor = mydb.cursor()
        sql_select_Query = "select * from seccao"
        mycursor.execute(sql_select_Query)
        
        records = mycursor.fetchall()
        print("Total number of rows in table seccao: ", mycursor.rowcount)
        mydb.commit()
        print("\nPrinting each row")
        for row in records:
            try:
                for x in range(2):
                    self.ids["seccao_data"].add_widget(
                        OneLineListItem(
                            text=str(row[x]),
                            on_release=self.mais_info_seccao
                            )
                        )

            except Exception as b:
                print(b)

    dialog_info_seccao = None
            
    def mais_info_seccao(self,obj):
        self.titulo_info_seccao = ""
        self.titulo_info_seccao = obj.text
        try: 
            self.dialog_info = None
            if not self.dialog_info:
                ok_btn = MDRaisedButton(text="Ok", on_release=self.close_dialog_seccao_info)
                copy_btn = MDRaisedButton(text="Copiar", on_release=self.copy_dialog_seccao_info)
                print(self.titulo_info_seccao)
                self.dialog_info_seccao = MDDialog(
                    title = self.titulo_info_seccao,
                    content_cls = Content_seccao_info(),
                    type="custom",
                    buttons=[
                        copy_btn,
                        ok_btn,
                    ],
                )
            self.dialog_info_seccao.open()
        except Exception as k:
            print(k)

    def close_dialog_seccao_info(self,obj):
        self.dialog_info_seccao.dismiss()

    def copy_dialog_seccao_info(self,obj):
        try: 
            pyperclip.copy(self.titulo_info_seccao)
            self.dialog_info_seccao.dismiss()
        except Exception as e:
            Snackbar(text="Parece que esta função não se encontra disponível no seu sistema operativo!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()

    ############### limpa a lista de seccoes ###################

    def remove_seccao_list(self):
        print("removido")
        self.ids["seccao_data"].clear_widgets()


        ###### botoes flutuantes das opcoes ######

    spin = BooleanProperty(False)
    def spinner(self):
        self.spin = False
    def callback_options_seccao(self, instance):
        if self.perm == 0 or self.perm == 1:
            if instance.icon == 'refresh':
                self.spin = True
                Clock.schedule_once(lambda _: self.spinner(), 3)
                self.remove_seccao_list()
                self.make_seccao_list()
            if instance.icon == "pencil-plus-outline":
                self.show_seccao(self)
            if instance.icon == "pencil-minus-outline":
                self.show_seccao_remove(self)
            if instance.icon == "selection-search":
                self.show_seccao_search(self)

    #++++++++++++++++++++++++++ dialog box adicionar seccoes ++++++++++++++++++++++++++


    dialog_seccao = None
    dialog_seccao_remove = None
    dialog_seccao_search = None


    def close_dialog_seccao(self,obj):
        self.dialog_seccao.dismiss()

    def show_seccao(self, obj):
        if not self.dialog_seccao:
            close_btn = MDRaisedButton(text="Cancelar", on_release=self.close_dialog_seccao)
            alter_btn = MDRaisedButton(text="Adicionar", on_release=self.add_seccao, size_hint=(None,None), size= (100,100))

            self.dialog_seccao = MDDialog(
                title = "Adicionar uma Secção\n",
                content_cls = Content_seccao(),
                type="custom",
                buttons=[
                    close_btn,
                    alter_btn
                ],
            )
        self.dialog_seccao.open()

    def add_seccao(self, obj): ##############################################################################
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
            mycursor = mydb.cursor()
        
            nome_seccao = MDApp.get_running_app().nome_seccao
            print("nome seccao -> " + nome_seccao)
            id_responsavel = MDApp.get_running_app().id_responsavel
            print("id seccao -> " + id_responsavel)
            

            sql_query_add = "INSERT INTO `seccao`(`Nome da Secção`, `Responsável pela Secção`) VALUES ('" + nome_seccao + "','" + id_responsavel + "')"
            mycursor.execute(sql_query_add)
            mydb.commit()
            Snackbar(text="Secção inserida com sucesso!",duration = 1,snackbar_x="10dp", snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#00ad11"), pos_hint={"center_x":.5}).open()
            self.close_dialog_seccao(self)
            self.remove_seccao_list()
            self.make_seccao_list()
            MDApp.get_running_app().add_seccao_ok = True
        except Exception as erro_add:
            print(erro_add)
            if "1452" in str(erro_add):
                Snackbar(text="Não existe nenhum funcionário com esse id!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()
            if "1062 (23000)" in str(erro_add):
                Snackbar(text="Já existe uma secção com esse nome!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()
            if "concatenate" in str(erro_add):
                Snackbar(text="Os campos devem ser preenchidos!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()
            
    #-------------------------- dialog box remover seccao --------------------------


    def close_dialog_seccao_remove(self,obj):
        self.dialog_seccao_remove.dismiss()

    def show_seccao_remove(self, obj):
        if not self.dialog_seccao_remove:
            close_btn = MDRaisedButton(text="Cancelar", on_release=self.close_dialog_seccao_remove)
            alter_btn = MDRaisedButton(text="Remover", on_release=self.remove_seccao, size_hint=(None,None), size= (100,100))

            self.dialog_seccao_remove = MDDialog(
                title = "Remover uma Secção",
                content_cls = Content_seccao_remove(),
                type="custom",
                buttons=[
                    close_btn,
                    alter_btn
                ],
            )
        self.dialog_seccao_remove.open()


    def remove_seccao(self, obj):
        try:
            print(MDApp.get_running_app().remover_seccao)
            query_remover = "DELETE FROM `seccao` WHERE `Nome da Secção`='" + MDApp.get_running_app().remover_seccao + "'"
            print(query_remover)
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
            mycursor = mydb.cursor()
            mycursor.execute(query_remover)
            mydb.commit()
            MDApp.get_running_app().add_seccao_ok = True
            self.close_dialog_seccao_remove(obj)
            self.remove_seccao_list()
            self.make_seccao_list()
            Snackbar(text="Secção apagada com sucesso!",duration = 1,snackbar_x="10dp", snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#00ad11"), pos_hint={"center_x":.5}).open()
        except Exception as e:
            print(e)
            Snackbar(text="Não existe nenhuma secção com esse nome!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()
            
    #??????????????????????????????? dialog box filtrar seccao ????????????????????????????????????

    def close_dialog_seccao_search(self,obj):
        self.dialog_seccao_search.dismiss()

    def show_seccao_search(self, obj):
        self.remove_seccao_list()
        self.make_seccao_list()
        if not self.dialog_seccao_search:
            close_btn = MDRaisedButton(text="Cancelar", on_release=self.close_dialog_seccao_search)
            alter_btn = MDRaisedButton(text="Procurar", on_release=self.search_seccao, size_hint=(None,None), size= (100,100))

            self.dialog_seccao_search = MDDialog(
                title = "Pesquisar uma Secção",
                content_cls = Content_seccao_search(),
                type="custom",
                buttons=[
                    close_btn,
                    alter_btn
                ],
            )
        self.dialog_seccao_search.open()

    def search_seccao(self, obj):

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
        mycursor = mydb.cursor()
        sql_search_Query = "SELECT * FROM `seccao` WHERE `Nome da Secção` REGEXP '" + MDApp.get_running_app().search_seccao + "'"
        mycursor.execute(sql_search_Query)
        records = mycursor.fetchall()
        print("Total number of rows in table: ", mycursor.rowcount)
        mydb.commit()
        self.remove_seccao_list()
        print("\nPrinting each row")
        self.close_dialog_seccao_search(self)
        for row in records:
            indx =+ 1
            try:
                for x in range(2):
                    self.ids["seccao_data"].add_widget(
                        OneLineListItem(
                            text=str(row[x]),
                            on_release=self.mais_info
                            )
                        )
                
            except Exception as b:
                print(b)
                self.close_dialog_seccao_search(self)
















################################     EMPREGADOS EMPREGADOS   #######################################

    def make_empregados_list(self):
        
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
        mycursor = mydb.cursor()
        
        if self.perm == 0 or self.perm == 1:
            sql_select_Query = "SELECT Nome, ID, Cargo,Estado,Secção,Salario FROM `trabalhadores`;"
        else:
            sql_select_Query = "Select Nome, ID, Cargo, Estado, Secção, Salario FROM `trabalhadores` WHERE Secção = '" + self.seccao_utilizador + "'"
        mycursor.execute(sql_select_Query)
        
        records = mycursor.fetchall()
        print("Total number of rows in table empregados: ", mycursor.rowcount)
        mydb.commit()
        
        print("\nPrinting each row")
        for row in records:
                try:
                    for x in range(6):
                        print(row[2])
                        if int(row[2]) >= self.perm:
                            self.ids["empregados_data"].add_widget(
                                OneLineListItem(
                                    text=str(row[x]),
                                    on_release=self.mais_info_empregados
                                    )
                                )

                except Exception as b:
                    print(b)


    dialog_info_empregados = None
    ####################### + que da informações sobre as seccoes
    def mais_info_empregados(self, obj):
        self.titulo_info_empregados = ""
        self.titulo_info_empregados = obj.text
        try: 
            self.dialog_info = None
            if not self.dialog_info:
                ok_btn = MDRaisedButton(text="Ok", on_release=self.close_dialog_empregados_info)
                copy_btn = MDRaisedButton(text="Copiar", on_release=self.copy_dialog_empregados_info)
                print(self.titulo_info_empregados)
                self.dialog_info_empregados = MDDialog(
                    title = self.titulo_info_empregados,
                    content_cls = Content_empregados_info(),
                    type="custom",
                    buttons=[
                        copy_btn,
                        ok_btn,
                    ],
                )
            self.dialog_info_empregados.open()
            


        except Exception as erro_info:
            print(erro_info)

    def close_dialog_empregados_info(self,obj):
        self.dialog_info_empregados.dismiss()

    def copy_dialog_empregados_info(self,obj):
        try: 
            pyperclip.copy(self.titulo_info_empregados)
            self.dialog_info_empregados.dismiss()
        except Exception as e:
            Snackbar(text="Parece que esta função não se encontra disponível no seu sistema operativo!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()


    ############### limpa a lista de seccoes ###################

    def remove_empregados_list(self):
        print("removido")
        self.ids["empregados_data"].clear_widgets()


        ###### botoes flutuantes das opcoes ######

    spin = BooleanProperty(False)
    def spinner(self):
        self.spin = False
    def callback_options_empregados(self, instance):
        if instance.icon == 'refresh':
            self.spin = True
            Clock.schedule_once(lambda _: self.spinner(), 3)
            self.remove_empregados_list()
            self.make_empregados_list()
        if instance.icon == "pencil-plus-outline":
            self.show_empregados(self)
        if instance.icon == "pencil-minus-outline":
            self.show_empregados_remove(self)
        if instance.icon == "selection-search":
            self.show_empregados_search(self)

    #++++++++++++++++++++++++++ dialog box adicionar seccoes ++++++++++++++++++++++++++


    dialog_empregados = None
    dialog_empregados_remove = None
    dialog_empregados_search = None


    def close_dialog_empregados(self,obj):
        self.dialog_empregados.dismiss()

    def show_empregados(self, obj):
        if not self.dialog_empregados:
            close_btn = MDRaisedButton(text="Cancelar", on_release=self.close_dialog_empregados)
            alter_btn = MDRaisedButton(text="Adicionar", on_release=self.add_empregados, size_hint=(None,None), size= (100,100))

            self.dialog_empregados = MDDialog(
                title = "Adicionar um Empregado",
                content_cls = Content_empregados(),
                type="custom",
                buttons=[
                    close_btn,
                    alter_btn
                ],
            )
        self.dialog_empregados.open()

    def add_empregados(self, obj): ##############################################################################
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
            mycursor = mydb.cursor()
        
            nome_empregados = MDApp.get_running_app().nome_empregados
            cargo_empregados = MDApp.get_running_app().cargo_empregados
            estado_empregados = MDApp.get_running_app().estado_empregados
            salario_empregados = MDApp.get_running_app().salario_empregados
            password_empregados = MDApp.get_running_app().password_empregados
            seccao_empregados = MDApp.get_running_app().seccao_empregados
            
           
            pass_encripted = cryptocode.encrypt(password_empregados, "wow")
            

            sql_query_add = "INSERT INTO `trabalhadores` VALUES (NULL,'" + nome_empregados + "','" + cargo_empregados + "','" + pass_encripted + "','" + estado_empregados + "','" + salario_empregados + "','" + seccao_empregados + "')"
            mycursor.execute(sql_query_add)
            mydb.commit()
            Snackbar(text="Empregado inserida com sucesso!",duration = 1,snackbar_x="10dp", snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#00ad11"), pos_hint={"center_x":.5}).open()
            self.close_dialog_empregados(self)
            self.remove_empregados_list()
            self.make_empregados_list()
            MDApp.get_running_app().add_empregados_ok = True
        except Exception as erro_add:
            print(erro_add)
            if "concatenate" in str(erro_add):
                Snackbar(text="Os campos devem ser preenchidos!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()
            if "1452 (23000)" in str(erro_add):
                Snackbar(text="Essa secção não existe!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()
            
            
    #-------------------------- dialog box remover empregados --------------------------


    def close_dialog_empregados_remove(self,obj):
        self.dialog_empregados_remove.dismiss()

    def show_empregados_remove(self, obj):
        if not self.dialog_empregados_remove:
            close_btn = MDRaisedButton(text="Cancelar", on_release=self.close_dialog_empregados_remove)
            alter_btn = MDRaisedButton(text="Remover", on_release=self.remove_empregados, size_hint=(None,None), size= (100,100))

            self.dialog_empregados_remove = MDDialog(
                title = "Remover um Empregado",
                content_cls = Content_empregados_remove(),
                type="custom",
                buttons=[
                    close_btn,
                    alter_btn
                ],
            )
        self.dialog_empregados_remove.open()


    def remove_empregados(self, obj):
        wm = MDApp.get_running_app().root
        try:
            print(MDApp.get_running_app().remover_empregados)
            id_empregado_remover = MDApp.get_running_app().remover_empregados
            if id_empregado_remover == 5000:
                Snackbar(text="Esse empregado não pode ser apagado!!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()

            else:
                query_remover = "DELETE FROM `trabalhadores` WHERE `id`='" + MDApp.get_running_app().remover_empregados + "'"
                print(query_remover)
                mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
                mycursor = mydb.cursor()
                mycursor.execute(query_remover)
                mydb.commit()
                if MDApp.get_running_app().remover_empregados ==  Login.username:
                    wm.current = "Login"
                MDApp.get_running_app().add_empregados_ok = True
                self.close_dialog_empregados_remove(obj)
                self.remove_empregados_list()
                self.make_empregados_list()
                Snackbar(text="Empregado removido com sucesso!",duration = 1,snackbar_x="10dp", snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#00ad11"), pos_hint={"center_x":.5}).open()
                
        except Exception as e:
            print(e)
            if "1451 (23000): Cannot delete or update a parent row:" in str(e):
                Snackbar(text="Não é possível remover esse empregado pois é responsável por uma secção!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()
            

    #??????????????????????????????? dialog box filtrar empregados ????????????????????????????????????

    def close_dialog_empregados_search(self,obj):
        self.dialog_empregados_search.dismiss()

    def show_empregados_search(self, obj):
        self.remove_empregados_list()
        self.make_empregados_list()
        if not self.dialog_empregados_search:
            close_btn = MDRaisedButton(text="Cancelar", on_release=self.close_dialog_empregados_search)
            alter_btn = MDRaisedButton(text="Procurar", on_release=self.search_empregados, size_hint=(None,None), size= (100,100))

            self.dialog_empregados_search = MDDialog(
                title = "Pesquisar um Empregado",
                content_cls = Content_empregados_search(),
                type="custom",
                buttons=[
                    close_btn,
                    alter_btn
                ],
            )
        self.dialog_empregados_search.open()

    def search_empregados(self, obj):

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
        mycursor = mydb.cursor()
        sql_search_Query = "SELECT Nome, ID, Cargo,Estado,Secção,Salario FROM `trabalhadores` WHERE `Nome` REGEXP '" + MDApp.get_running_app().search_empregados + "'"
        mycursor.execute(sql_search_Query)
        records = mycursor.fetchall()
        print("Total number of rows in table: ", mycursor.rowcount)
        mydb.commit()
        self.remove_empregados_list()
        print("\nPrinting each row")
        self.close_dialog_empregados_search(self)
        for row in records:
            try:
                for x in range(6):
                    self.ids["empregados_data"].add_widget(
                        OneLineListItem(
                            text=str(row[x]),
                            on_release=self.mais_info
                            )
                        )
                
            except Exception as b:
                print(b)
                self.close_dialog_empregados_search(self)




















###################### PRODUTOS PRODUTOS ######################################

    def make_produtos_list(self):
        MDApp.get_running_app().seccao_add_text = "Secção"
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
        mycursor = mydb.cursor()
        if self.perm == 0 or self.perm == 1:
            sql_select_Query = "select * from produtos"
        else:
            sql_select_Query = "select * from produtos where Seccao='" + self.seccao_utilizador + "'" 
        mycursor.execute(sql_select_Query)
        records = mycursor.fetchall()
        print("Total number of rows in table produtos: ", mycursor.rowcount)
        mydb.commit()
        print("\nPrinting each row")
        for row in records:
            try:
                for x in range(7):
                    self.ids["produtos_data"].add_widget(
                        OneLineListItem(
                            text=str(row[x]),
                            on_release=self.mais_info_produtos
                            )
                        )

            except Exception as b:
                print(b)

    dialog_info_produtos = None
    ####################### + que da informações sobre os produtos
    def mais_info_produtos(self, obj):
        self.titulo_info_produtos = ""
        self.titulo_info_produtos = obj.text
        try: 
            self.dialog_info = None
            if not self.dialog_info:
                ok_btn = MDRaisedButton(text="Ok", on_release=self.close_dialog_produtos_info)
                copy_btn = MDRaisedButton(text="Copiar", on_release=self.copy_dialog_produtos_info)
                print(self.titulo_info_produtos)
                self.dialog_info_produtos = MDDialog(
                    title = self.titulo_info_produtos,
                    content_cls = Content_produtos_info(),
                    type="custom",
                    buttons=[
                        copy_btn,
                        ok_btn,
                    ],
                )
            self.dialog_info_produtos.open()
            


        except Exception as erro_info:
            print(erro_info)

    def close_dialog_produtos_info(self,obj):
        self.dialog_info_produtos.dismiss()

    def copy_dialog_produtos_info(self,obj):
        try: 
            print(self.titulo_info_produtos)
            self.dialog_info_produtos.dismiss()
        except Exception as e:
            print("erro: " + e)

    ############### limpa a lista de produtos ###################

    def remove_produtos_list(self):
        print("removido")
        self.ids["produtos_data"].clear_widgets()


        ###### botoes flutuantes das opcoes ######

    spin = BooleanProperty(False)
    def spinner(self):
        self.spin = False
    def callback_options_produtos(self, instance):
        if instance.icon == 'refresh':
            self.spin = True
            Clock.schedule_once(lambda _: self.spinner(), 3)
            self.remove_produtos_list()
            self.make_produtos_list()
        if instance.icon == "pencil-plus-outline":
            self.show_produtos(self)
        if instance.icon == "pencil-minus-outline":
            self.show_produtos_remove(self)
        if instance.icon == "selection-search":
            self.show_produtos_search(self)

    #++++++++++++++++++++++++++ dialog box adicionar produtos ++++++++++++++++++++++++++


    dialog_produtos = None
    dialog_produtos_remove = None
    dialog_produtos_search = None


    def close_dialog_produtos(self,obj):
        self.dialog_produtos.dismiss()

    def show_produtos(self, obj):
        if not self.dialog_produtos:
            close_btn = MDRaisedButton(text="Cancelar", on_release=self.close_dialog_produtos)
            alter_btn = MDRaisedButton(text="Adicionar", on_release=self.add_produtos, size_hint=(None,None), size= (100,100))

            self.dialog_produtos = MDDialog(
                title = "Adicionar um produto",
                content_cls = Content_produtos(),
                type="custom",
                buttons=[
                    close_btn,
                    alter_btn
                ],
            )
        self.dialog_produtos.open()

    def add_produtos(self, obj): ##############################################################################
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
            mycursor = mydb.cursor()
        

            nome_produtos = MDApp.get_running_app().nome_produtos
            id_produtos = MDApp.get_running_app().id_produtos
            seccao_produtos = MDApp.get_running_app().seccao_produtos
            preco_produtos = MDApp.get_running_app().preco_produtos
            stock_produtos = MDApp.get_running_app().stock_produtos
            fornecedor_produtos = MDApp.get_running_app().fornecedor_produtos
            desc_produtos = MDApp.get_running_app().desc_produtos
           
        
            if float(preco_produtos) < 0:
                Snackbar(text="O produto não pode ter preço negativo!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()

            elif float(stock_produtos) < 0:
                Snackbar(text="O produto não pode ser inserido com stock negativo!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()

            else:
                if self.perm == 0 or self.perm == 1:
                    sql_query_add = "INSERT INTO `produtos` VALUES ('" + id_produtos + "','" + nome_produtos + "','" + seccao_produtos + "','" + preco_produtos + "','" + stock_produtos + "','" + fornecedor_produtos + "','" + desc_produtos + "')"
                else:
                    sql_query_add = "INSERT INTO `produtos` VALUES ('" + id_produtos + "','" + nome_produtos + "','" + self.seccao_utilizador + "','" + preco_produtos + "','" + stock_produtos + "','" + fornecedor_produtos + "','" + desc_produtos + "')"
                mycursor.execute(sql_query_add)
                mydb.commit()
                Snackbar(text="Produto inserido com sucesso!",duration = 1,snackbar_x="10dp", snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#00ad11"), pos_hint={"center_x":.5}).open()
                self.close_dialog_produtos(self)
                self.remove_produtos_list()
                self.make_produtos_list()
                MDApp.get_running_app().add_produtos_ok = True

        except Exception as erro_add:
            print(erro_add)
            if "1406 (22001): Data too long for column 'ID'" in str(erro_add):
                Snackbar(text="O ID do produto é demasiado grande!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()
            
            elif "1062" in str(erro_add):
                Snackbar(text="Já existe um produto com esse ID!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()
            
            elif "1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`projeto_m16`.`produtos`, CONSTRAINT `Produtos_ibfk_1` FOREIGN KEY (`Seccao`) REFERENCES `seccao` (`Nome da Secção`))" in str(erro_add):
                Snackbar(text="Essa secção não existe!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()

            elif "1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`projeto_m16`.`produtos`, CONSTRAINT `Produtos_ibfk_2` FOREIGN KEY (`Fornecedor`) REFERENCES `fornecedores` (`Nome`))" in str(erro_add):
                Snackbar(text="Esse fornecedor não existe!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()
            
            elif "1366 (22007):" in str(erro_add):
                Snackbar(text="Deve inserir números!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()

            elif "concatenate" in str(erro_add):
                Snackbar(text="Os campos devem ser preenchidos!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()
            else:
                Snackbar(text="Ocorreu um erro inesperado reveja os dados e tente novamente!",snackbar_x="10dp",duration = 2, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()

            
    #-------------------------- dialog box remover produtos --------------------------


    def close_dialog_produtos_remove(self,obj):
        self.dialog_produtos_remove.dismiss()

    def show_produtos_remove(self, obj):
        if not self.dialog_produtos_remove:
            close_btn = MDRaisedButton(text="Cancelar", on_release=self.close_dialog_produtos_remove)
            alter_btn = MDRaisedButton(text="Remover", on_release=self.remove_produtos, size_hint=(None,None), size= (100,100))

            self.dialog_produtos_remove = MDDialog(
                title = "Remover um produto",
                content_cls = Content_produtos_remove(),
                type="custom",
                buttons=[
                    close_btn,
                    alter_btn
                ],
            )
        self.dialog_produtos_remove.open()


    def remove_produtos(self, obj):
        try:
            print(MDApp.get_running_app().remover_produtos)
            if self.perm == 1 or self.perm == 0:
                query_remover = "DELETE FROM `produtos` WHERE `id`='" + MDApp.get_running_app().remover_produtos + "'"
            else:
                query_remover = "DELETE FROM `produtos` WHERE `id`='" + MDApp.get_running_app().remover_produtos + "' and Seccao = '" + self.seccao_utilizador + "'"
            print(query_remover)
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
            mycursor = mydb.cursor()
            mycursor.execute(query_remover)
            mydb.commit()
            MDApp.get_running_app().add_produtos_ok = True
            self.close_dialog_produtos_remove(obj)
            self.remove_produtos_list()
            self.make_produtos_list()
            Snackbar(text="Produto apagado com sucesso!",duration = 1,snackbar_x="10dp", snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#00ad11"), pos_hint={"center_x":.5}).open()
        except Exception as e:
            print(e)
            Snackbar(text="Não existe nenhum produto com esse ID!",snackbar_x="10dp",duration = 1, snackbar_y="10dp", size_hint_x=.9,bg_color=get_color_from_hex("#b80000"), pos_hint={"center_x":.5,}).open()

    #??????????????????????????????? dialog box filtrar produtos ????????????????????????????????????

    def close_dialog_produtos_search(self,obj):
        self.dialog_produtos_search.dismiss()

    def show_produtos_search(self, obj):
        self.remove_produtos_list()
        self.make_produtos_list()
        if not self.dialog_produtos_search:
            close_btn = MDRaisedButton(text="Cancelar", on_release=self.close_dialog_produtos_search)
            alter_btn = MDRaisedButton(text="Procurar", on_release=self.search_produtos, size_hint=(None,None), size= (100,100))

            self.dialog_produtos_search = MDDialog(
                title = "Pesquisar um Produto",
                content_cls = Content_produtos_search(),
                type="custom",
                buttons=[
                    close_btn,
                    alter_btn
                ],
            )
        self.dialog_produtos_search.open()

    def search_produtos(self, obj):

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
        mycursor = mydb.cursor()
        if self.perm == 0 or self.perm == 1:
            sql_search_Query = "SELECT * FROM `produtos` WHERE `Nome` REGEXP '" + MDApp.get_running_app().search_produtos + "'"
        else:
            sql_search_Query = "SELECT * FROM `produtos` WHERE `Nome` REGEXP '" + MDApp.get_running_app().search_produtos + "' and produtos.Seccao ='" + self.seccao_utilizador + "'"
        
        mycursor.execute(sql_search_Query)
        records = mycursor.fetchall()
        print("Total number of rows in table: ", mycursor.rowcount)
        mydb.commit()
        self.remove_produtos_list()
        print("\nPrinting each row")
        self.close_dialog_produtos_search(self)
        for row in records:
            try:
                for x in range(7):
                    self.ids["produtos_data"].add_widget(
                        OneLineListItem(
                            text=str(row[x]),
                            on_release=self.mais_info
                            )
                        )
            except Exception as b:
                print(b)
                self.close_dialog_produtos_search(self)

























######################################## ENCOMENDAS ENCOMENDAS ########################################

    def make_encomendas_list(self):
        print("encomendas")
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
        mycursor = mydb.cursor()
        sql_select_Query = "select * from encomendas"
        mycursor.execute(sql_select_Query)
        print("db requested")
        records = mycursor.fetchall()
        print("Total number of rows in table encomendas: ", mycursor.rowcount)
        
        mydb.commit()
        print("\nPrinting each row")
        for row in records:
            conteudo_encomenda = ""
            try:
                mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
                mycursor = mydb.cursor()
                conteudo_encomenda = ""


                mycursor.execute("select id_produto, quantidade from detalhes_encomenda where id_encomenda='" + row[0] + "'")

                resultados = mycursor.fetchall()
                mydb.commit()
                print(resultados)
                i = 0
                id_produto = resultados[1]
                for produto_id in resultados:
                    mycursor.execute("select nome from produtos where id='" + produto_id[0] + "'")
                    resultados_nome = mycursor.fetchall()
                    print(resultados_nome)
                    mydb.commit()
                    conteudo_encomenda = conteudo_encomenda + resultados_nome[0][0] + ", " + resultados[0][0] + ", x" + str(resultados[0][1]) + " | "
                    
                for x in range(7):
                    if x == 1:
                        self.ids["encomendas_data"].add_widget(
                            OneLineListItem(
                                text=conteudo_encomenda,
                                on_release=self.mais_info_encomendas
                                )
                            )
                        self.ids["encomendas_data"].add_widget(
                            OneLineListItem(
                                text=str(row[x]),
                                on_release=self.mais_info_encomendas
                                )
                            )
                    else:
                        self.ids["encomendas_data"].add_widget(
                            OneLineListItem(
                                text=str(row[x]),
                                on_release=self.mais_info_encomendas
                                )
                            )
            except Exception as b:
                print(b)

    dialog_info_encomendas = None


    

    ####################### + que da informações sobre as seccoes
    def mais_info_encomendas(self, obj):
        self.titulo_info_encomendas = ""
        self.titulo_info_encomendas = obj.text
        try: 
            self.dialog_info = None
            if not self.dialog_info:
                ok_btn = MDRaisedButton(text="Ok", on_release=self.close_dialog_encomendas_info)
                copy_btn = MDRaisedButton(text="Copiar", on_release=self.copy_dialog_encomendas_info)
                print(self.titulo_info_encomendas)
                self.dialog_info_encomendas = MDDialog(
                    title = self.titulo_info_encomendas,
                    content_cls = Content_encomendas_info(),
                    type="custom",
                    buttons=[
                        copy_btn,
                        ok_btn,
                    ],
                )
            self.dialog_info_encomendas.open()
            


        except Exception as erro_info:
            print(erro_info)

    def close_dialog_encomendas_info(self,obj):
        self.dialog_info_encomendas.dismiss()

    def copy_dialog_encomendas_info(self,obj):
        try: 
            print(self.titulo_info_encomendas)
            self.dialog_info_encomendas.dismiss()
        except Exception as e:
            print("erro: " + e)
    def remove_encomendas_list(self):
        print("removido")
        self.ids["encomendas_data"].clear_widgets()

    def refresh_encomendas(self):
        Clock.schedule_interval(lambda _: self.refresh_encomendas, 60)
        self.remove_encomendas_list()
        self.make_encomendas_list()

































class ServersDown(Screen):
    print("ta aq")
    spin = BooleanProperty(False)
    def tryagain(self):
        wm = MDApp.get_running_app().root
        print("ok")
        try:
            self.spin = True
            Clock.schedule_once(lambda _: self.spinner(), 3)
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
            mycursor = mydb.cursor()
            database = True
        except Exception as a:
            database = False

        if database == True:
            wm.current = "Login"
    def spinner(self):
        self.spin = False    







class design(MDApp):

    seccao_add_text = StringProperty()
    seccao_add_disabled = BooleanProperty()

    provider_opacity = NumericProperty(1)
    provider_disable_box = BooleanProperty()
    provider_menu = BooleanProperty()


    produtos_menu = BooleanProperty()

    empregados_menu = BooleanProperty()
    empregados_disabled = BooleanProperty()
    empregados_opacity = NumericProperty()

    seccoes_menu = BooleanProperty()


    title = "Xenox Software de Gestão de Stocks"
    icon = "logo_xenox.png"
    data_providers = {
        'Adicionar fornecedores': 'pencil-plus-outline',
        'Remover fornecedores': 'pencil-minus-outline',
        'Pesquisar fornecedores': 'selection-search',
        'Atualizar fornecedores': 'refresh'
        }

    data_seccao = {
        'Adicionar secção': 'pencil-plus-outline',
        'Remover secção': 'pencil-minus-outline',
        'Pesquisar secção': 'selection-search',
        'Atualizar secção': 'refresh'
        }

    data_empregados = {
        'Adicionar empregado': 'pencil-plus-outline',
        'Remover empregado': 'pencil-minus-outline',
        'Pesquisar empregado': 'selection-search',
        'Atualizar empregado': 'refresh'
        }

    data_produtos = {
        'Adicionar produtos': 'pencil-plus-outline',
        'Remover produtos': 'pencil-minus-outline',
        'Pesquisar produtos': 'selection-search',
        'Atualizar produtos': 'refresh'
        }


    def change_theme(self):
        print("ya1")
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
            
        else:
            self.theme_cls.theme_style = "Dark"
            

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepPurple"
        ########## variaveis mudar pass
        self.pass_old_change = StringProperty("")
        self.pass_new_change = StringProperty("")
        ########## variaveis adicionar fornecedores
        self.provider_nome = StringProperty("")
        self.provider_morada = StringProperty("")
        self.provider_iban = StringProperty("")
        self.provider_nif = StringProperty("")
        self.provider_telefone = StringProperty("")
        self.provider_email = StringProperty("")

        ########## variaveis remover fornecedores
        self.remover_nome = StringProperty("")

        ########## variaveis procurar fornecedores
        self.search_nome = StringProperty("")
        
        ########## variaveis info fornecedores
        self.nome_info = StringProperty("")
        self.morada_info = StringProperty("")
        self.iban_info = StringProperty("")
        self.nif_info = StringProperty("")
        self.telefone_info = StringProperty("")
        self.email_info = StringProperty("")

        ########## variavel verificar se os campos estao certos ou nao
        self.add_provider_ok = False
        self.remove_provider_ok = False
        self.search_provider_ok = False








        ########## variaveis adicionar seccao

        self.nome_seccao = StringProperty("")
        self.id_responsavel = StringProperty("")


        ########## variaveis remover fornecedores
        self.remover_seccao = StringProperty("")

        ########## variaveis procurar fornecedores
        self.search_seccao = StringProperty("")
        
        ########## variaveis info fornecedores
        self.nome_seccao = StringProperty("")
        self.id_responsavel_info = StringProperty("")
    

        ########## variavel verificar se os campos estao certos ou nao
        self.add_seccao_ok = False
        self.remove_seccao_ok = False
        self.search_seccao_ok = False








        ########## variaveis adicionar empregados

        self.nome_empregados = StringProperty("")
        self.cargo_empregados = StringProperty("")
        self.password_empregado = StringProperty("")
        self.estado_empregados = StringProperty("")
        self.salario_empregados = StringProperty("")
        self.seccao_empregados = StringProperty("")
        self.password_empregados = StringProperty("")


        ########## variaveis remover fornecedores
        self.remover_empregados = StringProperty("")

        ########## variaveis procurar fornecedores
        self.search_empregados = StringProperty("")
        
        ########## variaveis info fornecedores
        self.nome_empregados = StringProperty("")
        self.id_responsavel_info = StringProperty("")
    

        ########## variavel verificar se os campos estao certos ou nao
        self.add_empregados_ok = False
        self.remove_empregados_ok = False
        self.search_empregados_ok = False








        ########## variaveis adicionar produtos

        self.nome_produtos = StringProperty('')
        self.id_produtos = StringProperty("") 
        self.seccao_produtos = StringProperty("")
        self.preco_produtos = StringProperty("")
        self.stock_produtos = StringProperty("")
        self.fornecedor_produtos = StringProperty("")
        self.desc_produtos = StringProperty("")


        ########## variaveis remover fornecedores
        self.remover_produtos = StringProperty("")

        ########## variaveis procurar fornecedores
        self.search_produtos = StringProperty("")
        
        ########## variaveis info fornecedores
        self.nome_produtos = StringProperty("")
        self.id_responsavel_info = StringProperty("")
    

        ########## variavel verificar se os campos estao certos ou nao
        self.add_produtos_ok = False
        self.remove_produtos_ok = False
        self.search_produtos_ok = False


        def test_db():
            wm = MDApp.get_running_app().root
            try:
                mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="projeto_m16")
                print("ta nice")
                if wm.current == "ServersDown":
                    wm.current = "Login"
                
            except Exception as a:
                wm.current = "ServersDown"
                print("ta down")
        Clock.schedule_interval(lambda _: test_db(), 10)
        test_db()


design().run()
