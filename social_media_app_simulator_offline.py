print('LOG:')
print(' ')
print(' ')
import os #para detectar si estas en linux o en windows y para trabajar con el sistema operativo
from pprint import saferepr # no me acuerdo para que servia
import stat #para cosas de sistemas operativos creo

import tkinter as tk # GUI
from tkinter import ttk, messagebox #messagebox para widgets desplegables
from tkinter.font import Font #fuentes especiales
from PIL import Image, ImageTk #para trabajar con imagenes

import io #para trabajar con imagenes, especificamente abrir archivos o algo asi
import base64 #para encriptar imagenes i eso
from tkinter import PhotoImage #para trabajar con imagenes

from timeit import * #timing de los bots a los que les puedes enviar mensajes (hitler, stalin, etc)
import time #timing de los bots a los que les puedes enviar mensajes (hitler, stalin, etc)


from math import * #para la caluladora del menu "mas opciones"

class Cuerpo():
    def __init__(self, window):
        super().__init__()

        self.wind = window
        self.wind.title("sergolo's social media app simulator offline. Created by sergoloPY. Open-source")
        # if os.name == 'nt':
        #     self.wind.state('zoomed')
        # else:
        #     pass
        #self.wind.minsize(1920, 1080)
        #self.wind.maxsize(1920, 1080)

        # Función para obtener imagen desde URL (no se utiliza) REQUIERE REQUESTS
        # def get_image_by_url(url):
        #     response = requests.get(url)
        #     image = Image.open(BytesIO(response.content))
        #     photo = ImageTk.PhotoImage(image)
        #     return photo    


        self.boton_pulsado_verificado = False
        self.boton_pulsado_menciones = False
        self.boton_pulsado_social_media_app_simulator = False
        self.boton_ajuste_notis_toplevel = True

        self.siguiendo_hitler = False
        self.siguiendo_kkk = False
        self.siguiendo_generic_doll = False
        self.siguiendo_browser = False
        self.frame_chat_kkk = 0
        self.response_user_msg_hitler_executed = False
        self.response_user_msg_kkk_executed = False
        self.response_user_msg_stalin_executed = False

        self.easter_egg_executed = False
        self.easter_egg_executed_kkk = False
        self.easter_egg_executed_stalin = False
        
        self.currently_executing_msg_hitler = False
        self.currently_executing_msg_kkk = False
        self.currently_executing_msg_stalin = False
        self.logeado = False
        
        self.next_row_of_post = 4
        
        self.user = {}
        self.user_actually_loged = []
        self.nombre_usuario_publico = 'Usuario'

        # MARK: ESTILOS
        self.titulo_frame_style = ttk.Style()
        font_size1 = 20
        buton_font1 = ("Berlin Sans FB", font_size1)
        self.titulo_frame_style.configure("Title.TLabelframe", font=buton_font1)

        # Esto si que funciona
        self.espaciado_interno = ttk.Style()
        font_size = 17
        buton_font2 = ("Berlin Sans FB", font_size)
        self.espaciado_interno.configure("Custom.TButton", padding=(0, 10), font=buton_font2)

        self.espaciado_interno_titulo_label = ttk.Style()
        font_size_titulo_label = 17
        buton_font_titulo_label = ("Berlin Sans FB", font_size_titulo_label)
        self.espaciado_interno_titulo_label.configure("Custom.TLabel", padding=(0, 10), font=buton_font_titulo_label)
        #pading entry usuario (defectuoso)
        _espaciado_interno_entry_usuario = ttk.Style() 
        _espaciado_interno_entry_usuario.configure("Padding_entry_usuario.TEntry", padding=(0,0,0,0))
        
        self.verification_style = ttk.Style()
        font_size2 = 14
        label_font1 = ("Berlin Sans FB", font_size2)
        self.verification_style.configure('Verification.TLabel', font=label_font1)

        self.verification_style2 = ttk.Style()
        font_size3 = 12
        label_font2 = ("Berlin Sans FB", font_size3)
        self.verification_style2.configure('Verification2.TLabel', font=label_font2)

        self.w_happening_but1_style = ttk.Style()
        self.w_happening_but1_style.configure("Categoria.TLabel", font=("Arial", 8), foreground='gray51', padding=(5, 0))
        self.w_happening_but1_style.configure("Nombre.TLabel", font=("Berlin Sans FB", 11), padding=(5, 0))
        self.w_happening_but1_style.configure("Cantidad.TLabel", font=("Arial", 8), foreground='gray51', padding=(5, 0))

        self.post_style = ttk.Style()
        self.post_style.configure("Usuario.TLabel", font=("Arial", 8), foreground='gray51')
        self.post_style.configure("Nombree.TLabel", font=("Berlin Sans FB", 11))

        self.w_happening_but_style = ttk.Style()
        self.w_happening_but_style.configure("padding.TButton", padding=(20, 20))

        self.mostrar_mas_style = ttk.Style()
        self.mostrar_mas_style.configure("mostrarMas.TButton", font=('Arial', 10), foreground='SteelBlue1')

        font_size3 = 8
        tk_style = ("Arial", font_size3)

        self.boton_foto_style = ttk.Style()
        font_size_boton_foto_style = 14
        label_font_boton_foto_style = ("Berlin Sans FB", font_size_boton_foto_style)
        self.boton_foto_style.configure('boton_foto.TButton', font=label_font_boton_foto_style)

        font_size_nombre_post = 7

        Categoria = 'Educación'
        Nombre = 'Porno furro'
        Cantidad = '500 mil posts'

        self.style_focus=ttk.Style()
        self.style_focus.configure("placeholder.TEntry", foreground="black")
        self.style_focus.map("placeholder.TEntry",
          foreground=[("focus", "black"), ("!focus", "grey")])
        

        # MARK: FRAMES
        
        self.menu_frame = ttk.LabelFrame(self.wind, text='menú', style="Title.TLabelframe")
        self.menu_frame.grid(row=0, column=0, sticky="ns")

        self.posts_frame = ttk.LabelFrame(self.wind)
        self.posts_frame.grid(row=0, column=5, sticky="ns")

        self.frame_para_ti_o_siguiendo = ttk.LabelFrame(self.posts_frame, text='INICIO')
        self.frame_para_ti_o_siguiendo.grid(row=0, column=0,sticky='ew') 

        frame_r = ttk.LabelFrame(self.wind)
        frame_r.grid(row=0, column=10, sticky='ns')

        self.frame_buscar_frame_r = ttk.LabelFrame(frame_r)
        self.frame_buscar_frame_r.grid(row=0, column=0)

        frame_verification = ttk.LabelFrame(frame_r)
        frame_verification.grid(row=2, column=0, pady=20, sticky='ns')

        frame_w_happening = ttk.LabelFrame(frame_r)
        frame_w_happening.grid(row=4, pady=10, column=0, sticky='ns')

        frame_follow = ttk.LabelFrame(frame_r)
        frame_follow.grid(row=8, column=0, pady=10, sticky='ns')

        self.frame_hitler = ttk.LabelFrame(frame_follow)
        self.frame_hitler.grid(row=3, column=0, pady=10, sticky='ew')

        self.frameKKK = ttk.LabelFrame(frame_follow)
        self.frameKKK.grid(row=4, column=0,pady=10, sticky='ew')

        self.frame_generic_doll = ttk.LabelFrame(frame_follow)
        self.frame_generic_doll.grid(row=5,column=0, pady=10, sticky='ew')

        self.frame_browser = ttk.LabelFrame(frame_follow)
        self.frame_browser.grid(row=6,column=0, pady=10, sticky='ew')
        
        self.frame_para_ti = ttk.LabelFrame(self.posts_frame, text='')
        self.frame_para_ti.grid(row=1, column=0, sticky='ns', pady=0, padx=0)

        
        
        
        
        

        frame_escribir_post = ttk.LabelFrame(self.frame_para_ti)
        frame_escribir_post.grid(row=0, column=1, pady=0, padx=0, sticky='ew')

        frame_post_airstrike_company = ttk.LabelFrame(self.frame_para_ti)
        frame_post_airstrike_company.grid(row=2, column=1, pady=0, padx=0, sticky='ew')

        frame_post1 = ttk.LabelFrame(self.frame_para_ti)
        frame_post1.grid(row=3, column=1, pady=0, padx=0, sticky='ew')

        
        # Crear los atributos entry_var y place_holder_text
        self.place_holder_text = 'Buscar en social media app simulator'
        self.entry_var = tk.StringVar()

        #MARK: IMAGENES
        #images encripted in base64
        verification_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAOnSURBVEhL3ZVfSFNRHMfvnc5ZzTa9c9Kc081d1oqam1uwZanbbKX9gYKyICqIgt4i+kNBUI+RRU9FQUFB9FBGL0FB9NJDhcLSVv5ZTrf5bzbNrGwjdzu/228XF9dl4EP0gcPvd77n3PO758/vHOq/g0abFbPZ7FgsV5zsDYZqilVM35Ili951+NsPYvO8yBpIoynVMQxTNhAdfUiqKSgczXEcxaVURUzX6ODAzunp6Qm+899SWlpa7t2w6a5CtYyDsrSwJEbKqMVqv4VdeORK9Qd5oTokLyoOFxSpB63VjlPYJErGjDQaTdnXJBfGKg83kxozVJY/87e93o0Sj7ygwEzn5t+nOFrGSbg8CSeRqtWqyLepiR1DQ0MR7CZOvWdjEGaxyrqGs1qtdSqVqiSXgM1ZMbDLn8PM19e5r9IElMVJL1d1td2D0l9BAo3A92KBJGgziEYj79FdMIRAlqqqTehSer3egm5WlioLt6M7G65x85YWCQHrPEKlPzr6GKyurIz64xoT5MrijhSde16r099EiYIcI4YOR0eO2h2Oht+DUUbW1Axr27RtBze7ca6A5Xr2ETnafboK4z2UBGrrPNfSY+URUP41o9jHT1fAziS+7UsRwM8huH1Nwx5vw1mop1m12notPvnJxigV/nB/sBllgfH42B2w4XDmCU//Pf/n0jypDCwc6abNW060tbWXtPnfnltfW3cc9Cqb/c5AZGgr6T4zEOoV2x9KoVDowYYjIoGMrOEFWK3OcB2C/CC87exs9dTW3AD9TaD7QqVp5au+UMSbolM/vozHKkAXY4bOOQJ2T/Mu8aVP5xAkKyQqaDqdzlDv8Z7Ba2gYrhu+8xzY1jhb0+PsP3AgY8kF3G7PoXQnlmVXoEzJZLJ803JzI2w+SnNCvk3B9z7fxr1FBJR5hBPW09P9FF2yR1IpulQikfje3fX+8ZeJmAGlbPBLNTX1eXCcwCuIECgajfajS1UaKx3ozhutVmtElwoEAu3oCgiBANhAgLw/N5xOZyOZvYoX5oGeNT0AC2NMEnhxFhmnwuVyuQM9oWdY5SHPRIxhFP5QsMeHEg9rMp8dGYsfJkMoSY4vRpma/hzPTyaTCawKZMzI7/e/tKxgfadOHEOFDJMjYeLxSYvVZj9Jcph/MqpsjtuxsfHTEkmOJh2kZq2Lmvw4TIsFmRO4FeAqIute4XS6+OtJrFy4eGlhb3mS7YXr6hs6YXDIM7jHWlouP8HmfwmK+gm3bT3BJIskEgAAAABJRU5ErkJggg=='
        captura_perfil_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAYAAAAiwE4nAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAL5SURBVEhL7ZXLTxNBHMd3Zlv63kJbti+aAqXlIaWVYBXSKPEAiUaPevIgMR704h/gX2CMF0+euOnNx4WTIT7ixUhCiIpSHsFSHm1pqWkL3XZnnF0HlNDQLcHEGD/JZPL7zi/z3ZmdmR/zzwNorwij0Xgdsw0XWZVqGGBgwAAXeVvzQmp95UIul0vTtONBp9NddjpdMxqNJgohVEdOn7lpsjpyZptTCPQE52ja8WG321+S9lar1UZJKO+M3+8PS6YmiyPfGwwOSVotIO1rIopitihUCqVS6T0JsaTFYrFp3madBwDtZDOZDUmrhWLDQnH7tYgYDcZYoBJZYWAwlUx7GAQqiURigcqHwtK+Jga9oQKA+obL7RpxOp15t7ulf2UtPQ5YprHN63m2sb76gqYeSl2n1OvrnMhmtgaIiVmKschkrFbL3NL87Dk5QQF1GUr0hUJXIKu+hBAura3G76eSyS906O9E8QoHTkXGBEEoMBCOLC7HR5otTZ8xAgiJwsNvy0sTNK0migz7I4NP52OLUQyxmhxsCBAuyAMQN2AMtQyDct4W1/OPM9O3Zf2oeFtbu7kme9Jk5bNS3xcKX/V1dJynwzK9wdAtk4VPkPHVdn/3KyofjY5Azwfykmz5Ok9M6fV6E5Wr0u7vnJQ+rM3f9YZK9TEUPfuAs/JpyYxKNZFMOQuf6gudvEMlZTgcDq+0hVLzeDwBKitC2lpfoOcdDQ9Q9Wkzmxs9DKk/wd6ux/F4vK5K0OptmUimN8PtPt8wlfZR3bDRMkrOL9gu5ieppJjMZvIRmRQaOfM1Ku2j6luqM3D38sUdp9tln+I4zmiz2bxmzsxrNA16RG5euVwu0dQD6HT6JgGBMbVKVc5m0uNU3qPqPZT+HWBhM4PQDqlDcina5VcMftMxmQcgUqYEzEA1BMCERbT2Pbvhogl7VDUMD0SesACq5ckxWRO52cS8gjAuk6iEES6ToV1j4kwUhCuiWCmS8lUGALCkqb7Ofrr7M+c/fwyG+QEYORClGnE99gAAAABJRU5ErkJggg=='
        config_grande_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABsAAAAaCAYAAABGiCfwAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAG6SURBVEhL7ZZBSsNAFIaf4t6NG6HNDRR0obT2BgoKaoO5QUVEKUpvYKl6DFNbj2Ha4saFN2jqPWL+57wyJjNpApKF+MEwj5nJ/Jn3v0m7FMVQSSyrvhT+rlghz4LRmILxhGPPbZLjVDnOSyGxze1dCmczjp1qlT7e3zjOS6aY3x+QP3jhjSGCk3Vu2+RUKnR+eU2NvXrcavH4hPvOTVs9aQFiJp7852h1bf1H2z88VrNRdNd7SM1jLAurGDbGBmA6DbklwdhrMOIea1sXV2rGjLUakRaA1KEQTMWAMaRSfFyEVQw+APgldO8f6eDohAsFsaCvyUSdcA7SsrG1w2kxeSRzaLpH+rwp5SAlJg8lzRYRIB5hTMf2rJD7C8K+qXRJnPQxDD9VZEGJzsFbyyn06pKrYEujVC/mYYUJY+lDEEJ4WPKPHptjU2yoC0ladY9NWO9ZUiwLEbN5JWSU/lhF8GLGLQnG9HVyXawo0RR4S7yt3kwe6Q2+ZrGiNFPIR9XvD8k7a3Lc7X1fZHyIcSL9Q+y5p/E6l+etKNGFwBe9EhEXpdDvGTzyB0OOG/Uan6wI//+ufoUSxYi+ANWxfhXY5qMWAAAAAElFTkSuQmCC'
        config_peque_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABMAAAASCAYAAAC5DOVpAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAF6SURBVDhPrZNfSsNAEMZH8d0XX4QmN1DQB8U/N1BQUBvsDSoiSlF6A0vVY5haPYZpeo4m3iPmm84s020SX/zBkGFnd3bm28lKUUL/RGOyZJJSkk7Z70RtCsOA/VqQrI6tnb1ifWOTDf5fLFQWj8YUj78oDALK8pwr6z/1KGy16ObugY6PDks7KNen/O0/9uSkwClL3uMPV4XaydmFRIviefi6FMeaxSXDQWwAs1nG5oO172TCX+zt3t5LZM6qFMhlA7QGoavExhpahQRVuGTQAUAvZfDyRqfnl7S9u8++YvcsgLL11ao0si9qNbJxlYR00RdTkwDVyB8P/6xr04d1k3bU93XMsh/xBNyqVdjX0VGpa1NfH3FIBXg0kBCJENT+8cVhHMIBm0jbthoDN2d+siY0mb0AmNFIxYMWOZsP1uw+HSeHJOVbcJu1Ko2sQVfLmuR0P208+qTOdZv9wXA+qPjRUZH90TvRVbkv4rhDki4BXexLwm+mKH4BKpmIg++NXgYAAAAASUVORK5CYII='
        explorar_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAYAAAAiwE4nAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANrSURBVEhL3ZRfSFNRHMfvvTPntP1x98/uXF5XFnrLkTrd+jPLVRoiFRn0kkF/oYdegqinHoLoNYge6qEehP5AJERZBhVEpGkFJmnNUqdLp3eG07ZubvPe7rmdoNv+uPXnpQ+M3+HzO4cvd5zzQ/57UFiTYjabl5SUss1fI7H6t573bqawEDGRpD83TzMwx4daH7S3n4db0yJlYM3G2uO9fZ6z0hLsy5LlL6xxOvjXr7pWTExMjEGVkqSBlY61rYNDQ42CiH6lCdxLm4iWWDQ6plKpstQ5OcsiUWFnb19/OdgLvpo06k49fvTwjHw4U+yONbd0+SZOh1OfXDUbjkEdh8ViKbJVOEQ9YRZB1el0BthKn6pqxwGdkQpocWq6yGploU4KCHXVbukBoa6N7hdQp48Wp4NaIx1iV650QLUgBQUWBgSC3/r1rj1QJwSDVaaUZRtRQYywJcXP3vb3d0O9IOPjY6Ory9iLYB0VkGZZJkERqNUZ5K9ahKEtssgAbmL8MiIIc8FgkIEqIYrA6eBsA4KKKACqtPH5fO8EVOT9kwGr0WgkoI5DEchxU1YRxdTDw0NPoUqbcDgcoknKK700kaIoK9RxKAIpEh/FUFRLkskPpGIywDHSy573+/2DUMWhCNQb9D5Q6YKCBllkgN1etQNUFBFiMzMz07JMgCIwT6PukBeY6qhcMyBbrS4URSx7eXHxE6gW5uf3VF+/NaNQaTJNSpNpymaz1UGVHvsOHGwDgWBUgSkCdUoqKh1XQWB5leM6VElR/KWAl91dp8AwHvX5ECNl8W6odZ+ArYQsL1nVPTg8shlVYYQKQd5AnRRpjxKO4/xrnVUDAoLtAqGT3FRdWZmtvIhhcJ7/8pHn+VC103mYKVq6ezY0dzUc/vJ9YKNCBMNUBE2bAlOBgEd2CUj4wLMkmpqa9ubj5P4bN1trJBUV54Xg964C6c0RIxH+8yGcoE9+8I5uN5lIr2Gx5tzLF91X4B4FKSeKWsLt3nQkEhMqZ2c/53sGP7ikAyJJkF4TiT+Zj0U9Xc87L8HtSIW9+trQyMfdFtocNOhzT3d2PLsgSsD230ej0eTanetu/7h0LMtW/86YzAi9Xp+/tWFb8Efo3bZ7n2BLJu6W/ilgyjy4f8cAbjrDFCI56uwe2Pr3ZEvAJQRBvgGc/iT8lYhktgAAAABJRU5ErkJggg=='
        flechita_inversa_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABUAAAAWCAYAAAAvg9c4AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADRSURBVEhLY/wPBAxUBkxQmqpgGBv66u07KAs3IMnQqzfvMDR0T2OYOn85VAQ7INpQkIFT568Au9TByhQqigOAkhQhcOXG7f/BKYVg/PLNW6gobkDQUFINBAG8hsIMrOueSrSBIIDTUHINBAGcEfXq7Xsw/foN4SSEAaCGYwUw12aWN1PH+zAAMoxUgwmmUzFhIYZpHTVgNijhE5OjiC76QIaBDAWB7MQIBm11FTAbGyA6R4Fc3FCaBWYfOHYaTOMCJBfSIBeDLMAHRkt+agMGBgAyIBcEgb+fDwAAAABJRU5ErkJggg=='
        flechita_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABUAAAAWCAYAAAAvg9c4AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADWSURBVEhLY/wPBAxUBkxQmqpgGBn66u07KIt4gNfQqfOXMzR0TyPZYLyGOliZgmlSDSaYpECGgQwFgYbSLAYxYSEwGx8gGKYgQ0CGgUBWRQtxLga5lBjw8s3b/5nlzf+DUwr/X7lxGyqKHZCUo2BBAaKzEyMZHKFhjg5ITqeiIpAwFRMWBNNYAdi9RACQ9+u6pxLlfaIMBRkIMowYA0GAoKGkGggCeCPq6s07DPU908DJKjsxgkFbXQUqgx/gjagDx06TbCAIEJWjiMlFyGC05Kc2YGAAAI1LhoZCP97SAAAAAElFTkSuQmCC'
        hitler_encripted = 'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAjCAMAAAC0CkrjAAAAgVBMVEUJCQmBgYF3d3eXl5cPDw8LCwtwcHAFBQUCAgIMDAyKioqOjo4VFRVkZGSRkZGurq5VVVWUlJScnJyqqqpLS0uzs7NpaWleXl6GhoakpKRBQUGgoKB8fHy2trYfHx+6urozMzPW1tbr6+vi4uLAwMDNzc0mJibFxcUsLCzz8/P9/f12W4ygAAACqUlEQVQ4y01T6darKgxlEhQBGRzAua229rz/A97gd4ab1R9dbrKT7J2gCgmBIMpSqGvcV4WqsiqLEv0LARhS79Hqod3XFcF7Ud1x54oSsXUciPTeYduugomC3QEwBKTu2nWfB0Rww8WE+gMDsSgA7sPj9fx+fz1fC1mr/8NIMPW2/ny9fh58WvWXvMzFC3VZk7mf+cEzvtGf1m6YrXs7h207X8/X4/VddlbcAQPn33qNNnZbF7YlpGNbBpYHLipUQvFK7Xbo62ZpvDdGNlO0tx6QLaqyZJfmnLjUQWpI6QjYsh/81qQc65mQWE/L8TmPx3mG9i85cJd77eRMZpm6zwnVH8dYAXEBnUMuiGYpJZxE6sPitXV+VFUFKEOQWxZi1UT3RAIc5vGy/GKQnmFxy8beY6tJdFMXettaoorqN3n5z01Su+ANjlIr6BlEK34cE+9R97odZmz8NCXfKvHDnrdECDZGjLm1gyYmLdu0qxLkRtVvv1fdhVTzoW2HHtc1V9X9ucjTC6H23n8+2yT5YK1txwu0vCXNK1iyvdV8Arc/DUyvLyUKgIvcGRLQ9NBzztP5fL7OZqqvKlt8a14hADkITvhMH7AIj2a6GAOfcldgCVghJZlxnGU4v98zOatYmSsXmWKi3gA8x9pE/3ge0mA4BnYvNzS+pMlE4MbSRNmA1XXCvIdryJcgUOOpMZjoGUtnHKXYhTQlivtxLUSBAnUGdAa/MI7wEBsaQupCR/UbxvMyYkdrbmGfsHMxSjI1Ke+kaZlAkvAeMqTWOtd3VPZug5UNzdS/BYI+Bi49lfCH49r7mpvlaLquSRE2bgYj+rlOEwUeoPcU18vRbUsXpqGC7KEdOKaeOolhekpjhhe4hdArFIlurSbwGY5bSglt1N2xLJ9j67j6D+qFO4G5hsGIAAAAAElFTkSuQmCC'
        home_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAYAAAAiwE4nAAAACXBIWXMAAA7DAAAOwwHHb6hkAAADKUlEQVR4Xt2W3UsUYRTGd00t7UOiggrdJUqIICGjJNekuumiD4Mka73tJokoTFG66S6/iogg/ANa3fQiyyCKLjIVLOqikkT8aGezSEIWLKUvp9+xeWWaeVd3666Fh5k57znPc86Z876zHk+SP9M0U0FGJGIUcl2UZHjy7k+6e/YeKDlqChDNRdSbPEuCEadOn92ctXrdBzABJsE4tsYEw5Nz27ptZxkCfSBCdS0CS3yMta6boda1yTHO4w1xPzAg7qWlq5QrInnYulkbA+9I4to/iUJyHwyB97SuPh4Za0GEO/AbBAN/JUrgKxAl6zBVbUqEBNFmYt6IKHGHFowh00ycu8BTaeGlhqaKBYM0Dgi3iaiIx423WhLBaQSMIlbqdLZvAbbEvNvB4hnmOgx3i+JKsZGm+3JyRsE4tkxfdvZ3u6Bs+FBL+CLBJiRm3vYC2RYfGZz1caqYgWsQ9Pt8Oc/iVkrv2yGKQVSunBBL4fmxCDkQE1G6scNJKAMEl2vQ7BWqmHRussBiO0nFmXPF8lwUKPS8fN63pfN2+/7g8bK7mLx1DZc7NRX8wBZz2lM1jq4kDCO6UfkhtJT7ado0QLuGunt6A0Y0ukzD8xPblNOuq/Cr5WQqZwg3zN0b0T1er9cUYEuz1nSJa1+bTlCGRTL7piJ2FwUeUM3sYyh86x4Tuk++GHWNV9QmX6lhlyRc/DpBEfosbbOTBE8ca5Jn3peHCX2Ul18wFWoNz7rUVFfqTiHZNq7KdYLSKsFchUJaW32+SoZEVUorldhkTVXlBU2FMnwrnPZ4QyPZzTidb1y/eph2+hHLZ5BKmNhmhueF05ctVMxUy5S7viA6wQwcFVyJ+/2+CMYI77BDFhkeV2KY5YWngbkviyLStXQJi8utAE2nfptESInJkWeDcGaCNSDf+Y/AVSHv6K0QhsJtJ2nNBLcj4JOVhM9qkxBK9rJdsjnyvlg+Ma7TxDYIR1Fg1x1nxq4DmE9R7sEjpa9xlFZNAjVEcpXsJUaG4Y+TSNcKTiQ/r8Cwr2lPfPn+scfqGQy/5axEVazEKdj5Zg8LhukhA1arS+L/t/0CxAJAk5AIk/kAAAAASUVORK5CYII='
        kkk_encripted = 'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAjCAMAAAC0CkrjAAACOnpUWHRSYXcgcHJvZmlsZSB0eXBlIHhtcAAAWIXVmE1ypDAMhfc6xRzBSLYEx3GDvUvVLOf48wTpdNPppAlM1RhcxY8tPeuTpQ305+03/cLFKkYySrXegnYqetFkkYOyJjUdtMjEVurlcqlsmB80+kwySXGSECcLUWDb60Cxt2xwTGI5lhQhniEoAic2qVLCFLKM1ku2XuGqk2+nHQf/1lGLiWSCwcSMeKJWj0TysvBhXpmlQIhhoZITxxh1LeJrhEUX6i1iBMlwrDZfXAxWXLTC0LhKJ4MPvAVh3Bn3admAJzIx5ML3tp4n38HX72NAAEgKkFkHC7AcEHtBTO/roGGthMx5Aj2DaU5mVsWSSlI3jJIgD3QR5GxCVJ6EDnN4ioi/+VMID5wBDHphuEMd1yoDcJQn+AFbs45XdOLqhrgnOCZPsYMCEDnhInOy8f4SlR5Z96LSI+teVHpk3YLqoLNcngETThx1BPdVwaHkrftccK/qjbYW3Kt6I4Q36iAl4q7oTBiyDWjQCndvSZyImgNASmTk+nE4s991hm44S3uGwYcvP2bhmoSb1H0h0K0S1kZLc77Pfer8ZVMOt0H3H0fG/xFaw7QQ0QGh72BOh7Yd5gRoe2FaRLtnaSOiA0JfH8wJ0bZW2SnQ9rVMo2j/ov9bQbuxtBLRAaGvDuaUaNuq7CRoe1qmWbTj/d8O2pWlnYgOCD0/mJOibamy06D9vGUaRjva/y2hLSy7hJ79uyT/rbP8pjRb/jvSX95pME6WV0wkAAAACXBIWXMAAAsSAAALEgHS3X78AAAAh1BMVEXe3t7x8fE1NTXo6OggICDh4eEoKCgwMDAaGhrr6+skJCQsLCzv7+/t7e0+Pj7V1dXl5eXNzc1DQ0P09PTa2tr29vZISEgVFRU5OTk7Ozu+vr5YWFj4+PjS0tLGxsb7+/utra0PDw+1tbWMjIyVlZVQUFCenp7///+mpqZnZ2dhYWFzc3N/f3/T6dvhAAAC5UlEQVQ4yx1Ui7KrIAyMAgrylviu1lZtbXv+//tuvNEZZthlSSAL6LzMB93Wed7nus6d64e67wd3RdtCUVS6mL5VUeqqLOinKItcl/8DuCx4/yk5r7jUsuJVQR/XvCiIoQnmct8f/BqJI10hK6lJs6qIAB3nLc7tBUrJu2Mb9H/epVERLIsX4ushpXxw2Z1/D95xeXwkMXQORdfOCIuWsntUMp834km+rZWUFYnTYiGU+CsJl3JaxFeWvI12yiUvc5BHVIElNk5VJcsds2dxFD8Mi9OlI1jvs0gqKK/74/O0wrfT78mC/fFpciD5HkPApPC1PdcRs7ROfwAqxamdKpD5guL5BCPm78d7GKPZXgGVzeat5vBoPapxRNbM5dejfz0hClAipBQ1wd8oMhMaY8X0isgiwhhQ4B6t+Uh4/HnPkjKCmfMlkHIKowAM55jS1kG3YbTpplTIMM6gLFsgi0RXVo0lFCsDo5pMMQUBGQvGB0o8Y0w00YFeBEvpnozF3XtLBxQV7dAYE+6+htIjs9nNWBXOAEwldSWe2aCY9QO4BTOCrUpNjEHQ7BxAKaGUCeqAfMNks6SWsPx+IoTMjxjokpQNIW3QTWhslqlR7I8vzTfzekawSSQQ4wceB5h0b27N/dVtCTGFcRuBKrnbsGs6NWSqSe93OqvtJkKWidODsYylbHQkPgeTmvv7dvbrm2FifqVbiMJSDQQfM1Vze9/fT7c2wmY2roi4CmUUTiDdzEgx3e9jvbxRhfuyzh53YCGEP5CDZ+LWNLc09qfwJqnXGmf/AxWEWeFRY0BLkfzgjuP3+x5Pvywf0qGGo3ZApRqTUoZTSa1dFPU5+0hdwIRA6IbXusRxmZ972+dlmXN+/J3ntMwQ1x2qrpDO6ZyiHPK8dlqX+eXR+vNpySWanFuRn3RPDneDI3P3l3d12Tu60DInT2td0NqhJ88Pl/WH6xlwdQ2XKsmRnuvdUF+PQt1eUV/DP3o1Qp0eZQH+AAAAAElFTkSuQmCC'
        listas_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAYAAAAiwE4nAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANVSURBVEhL5ZbLaxNBHMdnZptH82iT3c2j2tomBGp9Va3WB0q9e5C20KPgQcSjBw/i41/w5kkQCmo9CR4VLAh6slWroCgIpZWaVNM86iZmX/5+4yTGbuJjPfpJJt/d787Od2YzmQwlv4ABFLAB1I2IagSvWwAeoyL8QgtaBiqKEtu+c9epleynk5DGmNQRYpKkSpLUKaq0Ra/VllQ5cvfJ40fnWgW3DOyKJlZAYFjwJsQLHx0wXl6XEssgNrywAiUS+FA4NrXsGtyjw9h9xKJmaS2bENfaM7Jv9CIEfhzaMXxVWH9Nb1//ybCSLCSSPYeE1YAJbQBf1jDq61cvznHDBctLi9PUtnRZjU8Jq4EjkFAGj49Q+L5Q/wmJMZ84bOAIhEpeEJpKpUa+Oy6h0HVKPeKsgSPQ4/FEqMRi0ai8WViugMntI9KfBPp8cVS/3x/iBhCPx9MwCYrdao/ZothhOVmGjvpF9TpUItLvA30+fxI1EAh0cwPQNC0fV5U3qiI/xRJT5LmYLM/H5OgzOJ+Px5S3g4Nbj4jqJJPJHIAlI8g62MZOODl+YtLGXk9MTF4R1l9z8OChKWxj9PDRB8Jq4JylAllR+sQhESsZB5c7BGbxT6AnqsNT8gVRQ+HQEDeaaBs4MDCwBwOwsfHxictdStLCEpYTJpZQNG40lzNnz07XQxVV3YLa6Q84Jl7bwFQqPcKHBKTTmVFhtyX/Ob+EizgeG4ZR42YL2gYiuPjCzcb09I3T/Zti+7H0qN27YpHgtkjQmwl4SF/QS7eg3pm5faEeWNG0Im/gT6hPmpu3ZvjNbhgbO3YK28C2hNXglyN0S6VaKaOWCoXn3GjCEQhPsIL6cmHhPjdcUCwWs6hftPV33GjCEQi9W0SdnX14nRsu+Fqtrlu2uQZTwDF5HIFfK5Ul1FK5tMoNF+RyuffUolXTNDVhNXAEwv/YHKppsWvccEFmcIj/eZcKa/e40UTrLYac0CBZg22CAfsGg1ikYtlWCXYWa8S2yrAsd2E9asMWg9EoIzRgM+KFxsR2AzdYtl3Or/Z+P/9By0Bk996R8+VyZdyybR1+Xjo0YIDWYH9WtUxzHR5X3jD0VV2vfTB0I8ckFvJ6/WlYmCLZleVLopn/DkK+AWbaOqQAQouLAAAAAElFTkSuQmCC'
        more_options_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAO+SURBVEhL3ZZLbBNHGMd3ZteO7X141/GubfyKYyhOiRHGNIgEUQwFiV4rkKh6KJVQL0hVxQGJI+JY9dATFxAnxAVRVYgD4oAqHlKgDZQkLW1QSngojjeuHzhx7Ky332wG6BJDgrn1Z61mvm/m2/88vtkx878D0XJFEEKCy+XKQLVqGMY48ZnAi3IRIPU3saIQCDgdDkcfiOQ8Hs9+X7fqeTKdjwUDgVmQaYQC6s+N+vy18fGxK5VKpUTDlvFWISrSL8vyCRDa3Wq1Zqv1JmcaDGawiRmT/JA1K031P5Jl/tSd4eHTVvBrvEmIxRh7OI6LK4ryPYhlQOSfWq12hheEa9BY1HX9SSqVyrk8ws6FRrNnYmJyBwlUNf/fDx+MbbXeshIg0u31eo8TkUgkMq2q6k+wbAdpc1u2fDTwlaQE8uRZu37DMHW3hy7VelEUj0Sj0TKIPNM07RLMLEGal3q9neS6D2+C2PTGzdmz1LUcmAloiIeDweDtcDjyDGZ1FER6SNNSj9UhKNqk4FOnREkKUddyJEW979eCozzPH4AZitT9zoiy+me8d+1FatqJRKP9ok97Guvp/Zq6OkbVAntFxf8HNe1LEosnDiETITiBj6mrYwoz+SuwrcaaNWErG21C+cLs9hZqGVOPJi9T13tiYqdbOE5qNqGZwkwYDmCTmhZuSbkQCse+o6aFIKu/iYo6Rk0LQfbf4r3dI9S0MEEHEsxF6jYhOOIGrb6EY7lUda7+GTWXwEgyEWNLFMQgP2JZhZpLYNOp68UUtV6xIb3pB0jL994fQigU+oCcp+zANivzbDNqGc2rMDKc2Zz9gro6Jt7TewgKLHulKiwftglVyqUxyDq2+rz+DXV1jD5b+gSxWO1ycHfhPCL7HpkMSQQ8U9DjuV27rWzphG2DQ0cKxeIWUh8dvf8j3F/2vSfKg0NDn3v9ocW+dLbUn04P0qZ3QvIF5uAdJgz2MHUth4jt2vPpFOmYzgyY8NXmadOq2JjJnoHY5tCO3C3qsmj7RU4mkym9PPc7qceiUcaBW1+O/PrLeRgDD7d2HUoOmlioz5MS6Ib7qsxLvmETIzf4zOfFQpzEv6CtEJlVIpFY15fOPLh+46blEz1dFyul4nVY7gK8WIEu7mazOUHE3W73noXGYsFgUHKhVjkIfeasoP+w4h3z8c7csZF749+yLJrv4pg8JCo5lC14SOwi/V/yV7lcPtloNO6RmHas6jIjOJ3OLIx8X71ev8pgNuER5XO1kr6JNjtA7CG57qn9GgzzL7AwNw7InubpAAAAAElFTkSuQmCC'
        msg_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANXSURBVEhL7ZZLTBNBGMdnZtttYWlpaSmPosESohgrIA8FAY0HNUZNBOPRu8SDiQSVg2cTLx70gAcTYzx4MEYvxsSD8ZWYKIkJPlaKPLQIpbSQ7WOX7sNvl7HpBppohRu/tDv/+fbr/nd2Z74p2mS9wbTNsqel5VC1f+vgfDRKJEmMyLIsIE1TESYWgjGD4UtTDQgmLGGIDRNswYhYoSUMwxQ7SrjIGP9laGJiYoymGqwydJRVJCGsYayKGiIsmJkM4AdYQwg+Rk+XmICvcYogrKo4QwjmVs4jVOlxBnmeH6VdM7sbG884Pb6FlvZ9D7ds2Rqk4X+CZdmipqbmY8Hmdq3UW6WdO3+B3twaBOobXoBhNBAItNJQwbS2tZ3SDXVjeA3ZJ6k/iiyqqiSRiuWZmZmvNFQwyWQyTqUJk6GmIUVvRFFMrEQKJ51KLVGJ8o6QEGTDDPE53RW/cpMKIbaUfkZlfkOEGDscCJhWOt2+tMPlC63E/55ip/uJPg9o14AAVJoN4T5YVVMW6wK1j7zl3o+IaHYY7SxX6hnBhFhp2prYOecw5H0ghKn2uN0jwV077tNT+Q1hzcLiZlycnX08zn/aK8Tma8q9rhuwropKXL5YSVn5VF399ks0HVVW+/v0m9FfAWNhaottlqHEYrR1IsQfzkjia5pmwmSo6UsXqPH7dxoBYHyMvybEow1Oju2HBCWysHjVUVYplHorpJSUua2PPCMJTcml+JH5yFz2vdntdgeVSAGoNBtarJYKvT1+4uSgEcgh/GP6XiIeCbgdRac97tI3iqLN+Mpc/Yn4fBBm5BxNy1LMcS4qTZgMWavNT2Vepqcmn06O80fBfFto7NsDGl4FlF+VStCw4Cgmw/VEEATTTP3DhhmKaVGg0sSGGeaWtryPVIViSuV/A0svu63lGprKV8f+7uuf+dBA1/5O1NO5d/Tlq5d3Ywuxn9KylJIzspQ7EfR6pV9JhQ+GDmzUy6KYFmZn50KZzLLY3tH1/PPXbz2XBy+iK4MDWZ9V9VLfUqhcF+4M33rT19fbRburDXW6Dxy8abNxvYjB1lQi+V2WMzFFkVMwQBkGpUABWLkp+GNgbHb6AUoUXMy4HlQdR1VVtf39u7dnw+HwlJG7ySaFgdBvyvM+VA79KIsAAAAASUVORK5CYII='
        notifications_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAYAAAAiwE4nAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAMFSURBVEhL3ZVLTBNBGMd3W9pt6dItbaF1aZu0UKi22Ehti1BeiSAJCWKQxMhVrybGxHjmRExMPBhvHjUGUSHRxJORIMbEEOIrEHlsKURAoQ2vslv6cGc6HJaWlq0X4y+Z/L/5z7f5ZnZ2ZrH/HhxpTmi6wmKz2ZrlCoWVZWOdGI6nCLl8Nr7PvWMW5seWl5eDKDUveQt6/f7rP+ZDD/mwKO0IoWljREuRAxPj4/eRlZOcBT3e+uE5ZrGXD/f1Ou2UWqV4kEwm46srK59ok/ny1k60b30jXAdydaWasYXZ6VYQF4THd+4lpT+RKtEZt5wu1yVkZ0VdalgDuVZbVc68Iwk0Nd+ExbTGHWTl5aAo6h6JBKmAX+vha7wkDLqSnrSTn63ImgGoxWYfgcZx8fvr+8BMwYyRdWxIbVmIfzaOulnJWKGMUDQBPemoegQNESTZaAsvUjVFVaSdTDIKclzMCnQzEn4DDRFEo7sMUP7Y3oBGFjIKbm/v1gKVFkll0CgAluVOoTA/YP9AIwhCgSxRoP1fRd0MBCukadqMQv7VciwKRZFKJvdSOE6ibgaCgjU1jgsoLBhjeVlQIsHlbrcbfnyHERSUSKXwvvT5zkagUQCUhlrgRUZRmsq0I0RQUEWSTqBKgviC80BTJOoSyg209Xx71stc8AdIJLFqoEww1NLd0/uWi3Gbif0EG0/E9/j6EmWxspxj2TCWSsErDPgxLrYpkxNqklRV8MVs36ZnTGBscnKKAnoYwSoaAi0T32d+NKDuXxFobMBejz7PeEsCw2Q2u5yu2n7wC+IHcBmh9L7/8LEDjHnrTg9YbZWtFovFt/F7fY6i1CZFcbFm8O49+Oyd27egHmAxmbD+q1fEbYterzfUnvHBc9nR2TWEbIiTp+tiLxwDbZAHDeUk7wzqPJ7u+cWfoyC2mM1YW1vga5m+3DH07IUstLQEc16NDGNNgUZxq8mF3V7dfrCSw+3xk6cpGQ9KzYuoWdlrHP1KpaqNP64kpVZ9XgwywwzDzKLhfxEM+wPxPeq9+XXcCgAAAABJRU5ErkJggg=='
        profile_big_encripted = 'iVBORw0KGgoAAAANSUhEUgAAACMAAAAoCAMAAABDwLOoAAAAIGNIUk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAADnUExURa+4vq63vbG5v7nBxsHIzsTL0LrBx9LY3OTo6+zv8u7x9MDHzOLl6fP1+PX3+rvDyOTn6/T2+bK7wdjc4cHIzezv8/X2+bC5v9LX3LO8wt3i5ra+xOPn6+To7LW9w+Hl6bG6wNfd4cnP1PHz9rjAxePn6sfO0rK7wM/V2rO7wcrQ1eXo7LrCx9bb39ne4sPKz87U2Nbc4Nje4r/HzNTa3ubq7e/y9fL0+Oru8fX3+b/Gy+Dk6PL1+LzDydzg5LC5vszT1/Dz9s/V2ePm6sPJz6+5vtDW2tvf47a+w7jAxufq7uns7/////XZPbMAAAABYktHREz3bxDzAAAAB3RJTUUH5wkIFRI0TJwu+QAAAVFJREFUOMvN02mfgVAUBvCSUeJeriVLhigiGQwh+75+/+8zk0Hh3F7P8/r/6zydUwzzv8M68RcBLvgR5AJ+KsQLYTEs8CE6iUQRdoKiERqJxck98RhMEkniJpkA+6bS0oNI6RTUO5NFnuegbAYwuTz2GJzPAaPkwpMpyCxgPp+MAJli6cmUikBppUy8KSvQy1dUD1Er4A61qjsMVzV40TXxjrBYo9xLr98QFus67agNo6kSTNSm0WDoMY3WV8swfYSitTvd726nrSkwYPVe3xoMEULDgdXv6dDdOX5E7Nt72WTEc+9kPJk+3WI6Gb+SSJO8pvnyUc8E8h5h5iXynECZyy5ZLFegWS0X7uYsDBpsudtcIwIHrR9tNphi8ObWiN2KEsVI4vZv3bs9bdTvsP3uahIHm2rsw/WfZo/UOk6hozOMPZ19zPl0NebFx1xMlvkBCSY6i4zNmg8AAAAldEVYdGRhdGU6Y3JlYXRlADIwMjMtMDktMDhUMjE6MTc6NTUrMDA6MDCdxjFyAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIzLTA5LTA4VDIxOjE3OjU1KzAwOjAw7JuJzgAAACh0RVh0ZGF0ZTp0aW1lc3RhbXAAMjAyMy0wOS0wOFQyMToxODo1MiswMDowMI8izRIAAAAASUVORK5CYII='
        profile_uno_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAJySURBVEhLvZVLaxNRFMfPuZNHm5igFhVDKVpcxtiWCJWupCvBlTQihZgwwWJwpd8gX0DcSCEu+kCC4AcQd+1CEITUZlEQCq1S8IFiIT4y6cw9nkkPRZlMEkrqD8I9/3Mn58/ce+4d+B+gjF0hIszn82eCWsdxYKCeSCQ+l0olLdMd6WriFjfN29MK1HUiGJI0IOJ3DfrFyMj5l93MOppkMhkjfixyj4tflpQXBbVAIPyoXC7vScaDkrEt8Wj0RkcDFw0p27JuiWqLr4lpmjECuiayMwqmC4XCSVEefE3QcVI8BPdVFwgMsu1xUR78TZQ6K2GvnJLRg68Jd5UlYU9wtzUl9OC/8Y6zKVFPkONsSejB12R4dPQdb/xHkV2gr/VGoybCgyGjh9XVVUqnU++B1BRL/zfmJtagHlcqlU+iPfiauFSrtW9j48ltXvEUAoYk/Rf0CxTNLywsv5VEWzqa3J+ZGZyvPNtJJi+uGAH1A4itEPYQaIffbcVqOk+Wl59uuc+93tiw5W8e2l4ruVzuOLtnuNAUadjmh96AYWyGw40v9bpqxmI6ZFkDp7k7Lrg3As+f45P/ygF4vrS0tCtlDvCY8E07oZDm+IBFJdU7CD81YXlxcbEqmRb/LBfftlcVYJEN2qx/T4QU4uT4RGp3bW2d93KfAxPTzKaRjLvu1S6pw4IEaiydvvShWl1vHYFWaxaLsydA450+GLRArqNtmpud5bpMy6T5O3STpyJu3D8wMhhy63KUzWaHgoZ6yHGnA3c4EBxUgQcqGFSTLPtv4OJ+Asi+okBTUlJHA9fnjsVhkUcD13eXKcbfAjqqHwDE/gAggd2dx830LAAAAABJRU5ErkJggg=='
        saves_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAZCAYAAAArK+5dAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANjSURBVEhLtZbbSxRRHMfnvjPO7uzOqqOrKaYiLhVhaIaJRUoUURIZSCL1GvjQQ75HRQ9B9Af0IIEE0YV6qJeCELyDFEZG99JSdMvLmuuuuzPT+Z09O+44GrtBH1h+5/c9M/s9l985u9T/hiYRw7JsqaYVtMYTCe1naO4Sx3HFhmEsk+6NmKRPT6abYzPw5gVM3YjP0zodp2hjzuuW1EQi8QV9kYm6w8mnksCXRyLRFZNm6zhOKFQ88scf3782km4Ly8Dvzz2tM0yvx+19E14IXVsOh1/IsnyOYRgBdTtGaZpmOBaLffAoSqmaq10N/VooClaV3xkeHOggj9jZXl5xU/bnzxcGAl1EypiKysrLMPvzXRdgprZVYUiEERmMYSbWYmtLRMoYtIxR0nRgM4Co6/qWD28FemcN4moksoqFNCwDNC88NbLmWZEyiEZXHBW3bsCwnMlQrCAICpEyBhnEIK6uxLY2YFiaYxnezwu8TKSM0ckeoKr9jYU0LAOO4yWILMu5sJAFqHSgeqh4LB7BQhqWgSjl+CAKAp+DhSxA+8ZDTJiG47xYBorbUwDRJbjcWMiClAFt4hNvwzLw5aoBiKIoZb3JyICDqJsmzMBmYhkU5mvbIMqKR8VCFqBLUYRooFsSC2msb7Ig4vr3KoofCxtAowygTyFJbfC8gCuPZmnbNQFYBim8infjDGifz3fU4y+Y3rG7dqY6GLwOWrIriegS8bJyLOc4pCkD64Wi4uIS0gTYtvb2UZOTnkIyOTVFzYQWu+vq63tQag1OlFzYwCWKjjPkmIFPVb0QJUnac6z1VOLZ875ayBv3N1AnTxzHd837T5Nnd9Xs1Xmer4JcknJw5THoEKFgm53DAAgGg92C7BvrHxjEefPBxpEnjx8wt3tuFVdXlvWCBrOp3lnz7sCh5kcMm6wigePxZqfjMOgfGKKmQ4uwzlRpSQklskb7w/v39qEUXbjmwsjwUOfKYqgC+sDk1fhE69JytA2edyseR4FsYpAcNSzJ65ej3Ozs7F0spIHu/88T42NlRZp6A3IwAlQ1Nw830kgZ2A5HU0NdH1oSFjW3/EFHN+i3txMTF/N88hUi/Z2Ww0fG0MaZiqK0EClj0L+REni3/UzHLEodZwGjaVonaf4zstvdRJoEivoDTzMUlOdM4HAAAAAASUVORK5CYII='
        stalin_encripted = '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'
        
        #desencriptar
        verification_decoded = base64.b64decode(verification_encripted)
        captura_perfil_decoded = base64.b64decode(captura_perfil_encripted)
        config_grande_decoded = base64.b64decode(config_grande_encripted)
        config_peque_decoded = base64.b64decode(config_peque_encripted)
        explorar_decoded = base64.b64decode(explorar_encripted)
        flechita_decoded = base64.b64decode(flechita_encripted)
        flechita_inversa_decoded = base64.b64decode(flechita_inversa_encripted)
        hitler_decoded = base64.b64decode(hitler_encripted)
        home_decoded = base64.b64decode(home_encripted)
        kkk_decoded = base64.b64decode(kkk_encripted)
        listas_decoded = base64.b64decode(listas_encripted)
        more_options_decoded = base64.b64decode(more_options_encripted)
        msg_decoded = base64.b64decode(msg_encripted)
        notifications_decoded = base64.b64decode(notifications_encripted)
        profile_big_decoded = base64.b64decode(profile_big_encripted)
        profile_uno_decoded = base64.b64decode(profile_uno_encripted)
        saves_decoded = base64.b64decode(saves_encripted)
        stalin_decoded = base64.b64decode(stalin_encripted)
        #convert to bytes string
        verification_bytes = io.BytesIO(verification_decoded)
        captura_perfil_bytes = io.BytesIO(captura_perfil_decoded)
        config_grande_bytes = io.BytesIO(config_grande_decoded)
        config_peque_bytes = io.BytesIO(config_peque_decoded)
        explorar_bytes = io.BytesIO(explorar_decoded)
        flechita_bytes = io.BytesIO(flechita_decoded)
        flechita_inversa_bytes = io.BytesIO(flechita_inversa_decoded)
        hitler_bytes = io.BytesIO(hitler_decoded)
        home_bytes = io.BytesIO(home_decoded)
        kkk_bytes = io.BytesIO(kkk_decoded)
        listas_bytes = io.BytesIO(listas_decoded)
        more_options_bytes = io.BytesIO(more_options_decoded)
        msg_bytes = io.BytesIO(msg_decoded)
        notifications_bytes = io.BytesIO(notifications_decoded)
        profile_big_bytes = io.BytesIO(profile_big_decoded)
        profile_uno_bytes = io.BytesIO(profile_uno_decoded)
        saves_bytes = io.BytesIO(saves_decoded)
        stalin_bytes = io.BytesIO(stalin_decoded)
        #convert bytes to pillow img
        verification_pil = Image.open(verification_bytes)
        captura_perfil_pil = Image.open(captura_perfil_bytes)
        config_grande_pil = Image.open(config_grande_bytes)
        config_peque_pil = Image.open(config_peque_bytes)
        explorar_pil = Image.open(explorar_bytes)
        flechita_pil = Image.open(flechita_bytes)
        flechita_inversa_pil = Image.open(flechita_inversa_bytes)
        hitler_pil = Image.open(hitler_bytes)
        home_pil = Image.open(home_bytes)
        kkk_pil = Image.open(kkk_bytes)
        listas_pil = Image.open(listas_bytes)
        more_options_pil = Image.open(more_options_bytes)
        msg_pil = Image.open(msg_bytes)
        notifications_pil = Image.open(notifications_bytes)
        profile_big_pil = Image.open(profile_big_bytes)
        profile_uno_pil = Image.open(profile_uno_bytes)
        saves_pil = Image.open(saves_bytes)
        stalin_pil = Image.open(stalin_bytes)
        #convert pil img to tkinter img
        


        verification_tk = ImageTk.PhotoImage(verification_pil)
        captura_perfil_tk = ImageTk.PhotoImage(captura_perfil_pil)
        config_grande_tk = ImageTk.PhotoImage(config_grande_pil)
        config_peque_tk = ImageTk.PhotoImage(config_peque_pil)
        explorar_tk = ImageTk.PhotoImage(explorar_pil)
        flechita_tk = ImageTk.PhotoImage(flechita_pil)
        flechita_inversa_tk = ImageTk.PhotoImage(flechita_inversa_pil)
        hitler_tk = ImageTk.PhotoImage(hitler_pil)
        home_tk = ImageTk.PhotoImage(home_pil)
        kkk_tk = ImageTk.PhotoImage(kkk_pil)
        listas_tk = ImageTk.PhotoImage(listas_pil)
        more_options_tk = ImageTk.PhotoImage(more_options_pil)
        msg_tk = ImageTk.PhotoImage(msg_pil)
        notifications_tk = ImageTk.PhotoImage(notifications_pil)
        profile_big_tk = ImageTk.PhotoImage(profile_big_pil)
        profile_uno_tk = ImageTk.PhotoImage(profile_uno_pil)
        saves_tk = ImageTk.PhotoImage(saves_pil)
        stalin_tk = ImageTk.PhotoImage(stalin_pil)
        #global variables
        #images encripted in base64
        verification_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAOnSURBVEhL3ZVfSFNRHMfvnc5ZzTa9c9Kc081d1oqam1uwZanbbKX9gYKyICqIgt4i+kNBUI+RRU9FQUFB9FBGL0FB9NJDhcLSVv5ZTrf5bzbNrGwjdzu/228XF9dl4EP0gcPvd77n3PO758/vHOq/g0abFbPZ7FgsV5zsDYZqilVM35Ili951+NsPYvO8yBpIoynVMQxTNhAdfUiqKSgczXEcxaVURUzX6ODAzunp6Qm+899SWlpa7t2w6a5CtYyDsrSwJEbKqMVqv4VdeORK9Qd5oTokLyoOFxSpB63VjlPYJErGjDQaTdnXJBfGKg83kxozVJY/87e93o0Sj7ygwEzn5t+nOFrGSbg8CSeRqtWqyLepiR1DQ0MR7CZOvWdjEGaxyrqGs1qtdSqVqiSXgM1ZMbDLn8PM19e5r9IElMVJL1d1td2D0l9BAo3A92KBJGgziEYj79FdMIRAlqqqTehSer3egm5WlioLt6M7G65x85YWCQHrPEKlPzr6GKyurIz64xoT5MrijhSde16r099EiYIcI4YOR0eO2h2Oht+DUUbW1Axr27RtBze7ca6A5Xr2ETnafboK4z2UBGrrPNfSY+URUP41o9jHT1fAziS+7UsRwM8huH1Nwx5vw1mop1m12notPvnJxigV/nB/sBllgfH42B2w4XDmCU//Pf/n0jypDCwc6abNW060tbWXtPnfnltfW3cc9Cqb/c5AZGgr6T4zEOoV2x9KoVDowYYjIoGMrOEFWK3OcB2C/CC87exs9dTW3AD9TaD7QqVp5au+UMSbolM/vozHKkAXY4bOOQJ2T/Mu8aVP5xAkKyQqaDqdzlDv8Z7Ba2gYrhu+8xzY1jhb0+PsP3AgY8kF3G7PoXQnlmVXoEzJZLJ803JzI2w+SnNCvk3B9z7fxr1FBJR5hBPW09P9FF2yR1IpulQikfje3fX+8ZeJmAGlbPBLNTX1eXCcwCuIECgajfajS1UaKx3ozhutVmtElwoEAu3oCgiBANhAgLw/N5xOZyOZvYoX5oGeNT0AC2NMEnhxFhmnwuVyuQM9oWdY5SHPRIxhFP5QsMeHEg9rMp8dGYsfJkMoSY4vRpma/hzPTyaTCawKZMzI7/e/tKxgfadOHEOFDJMjYeLxSYvVZj9Jcph/MqpsjtuxsfHTEkmOJh2kZq2Lmvw4TIsFmRO4FeAqIute4XS6+OtJrFy4eGlhb3mS7YXr6hs6YXDIM7jHWlouP8HmfwmK+gm3bT3BJIskEgAAAABJRU5ErkJggg=='
        captura_perfil_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAYAAAAiwE4nAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAL5SURBVEhL7ZXLTxNBHMd3Zlv63kJbti+aAqXlIaWVYBXSKPEAiUaPevIgMR704h/gX2CMF0+euOnNx4WTIT7ixUhCiIpSHsFSHm1pqWkL3XZnnF0HlNDQLcHEGD/JZPL7zi/z3ZmdmR/zzwNorwij0Xgdsw0XWZVqGGBgwAAXeVvzQmp95UIul0vTtONBp9NddjpdMxqNJgohVEdOn7lpsjpyZptTCPQE52ja8WG321+S9lar1UZJKO+M3+8PS6YmiyPfGwwOSVotIO1rIopitihUCqVS6T0JsaTFYrFp3madBwDtZDOZDUmrhWLDQnH7tYgYDcZYoBJZYWAwlUx7GAQqiURigcqHwtK+Jga9oQKA+obL7RpxOp15t7ulf2UtPQ5YprHN63m2sb76gqYeSl2n1OvrnMhmtgaIiVmKschkrFbL3NL87Dk5QQF1GUr0hUJXIKu+hBAura3G76eSyS906O9E8QoHTkXGBEEoMBCOLC7HR5otTZ8xAgiJwsNvy0sTNK0migz7I4NP52OLUQyxmhxsCBAuyAMQN2AMtQyDct4W1/OPM9O3Zf2oeFtbu7kme9Jk5bNS3xcKX/V1dJynwzK9wdAtk4VPkPHVdn/3KyofjY5Azwfykmz5Ok9M6fV6E5Wr0u7vnJQ+rM3f9YZK9TEUPfuAs/JpyYxKNZFMOQuf6gudvEMlZTgcDq+0hVLzeDwBKitC2lpfoOcdDQ9Q9Wkzmxs9DKk/wd6ux/F4vK5K0OptmUimN8PtPt8wlfZR3bDRMkrOL9gu5ieppJjMZvIRmRQaOfM1Ku2j6luqM3D38sUdp9tln+I4zmiz2bxmzsxrNA16RG5euVwu0dQD6HT6JgGBMbVKVc5m0uNU3qPqPZT+HWBhM4PQDqlDcina5VcMftMxmQcgUqYEzEA1BMCERbT2Pbvhogl7VDUMD0SesACq5ckxWRO52cS8gjAuk6iEES6ToV1j4kwUhCuiWCmS8lUGALCkqb7Ofrr7M+c/fwyG+QEYORClGnE99gAAAABJRU5ErkJggg=='
        config_grande_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABsAAAAaCAYAAABGiCfwAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAG6SURBVEhL7ZZBSsNAFIaf4t6NG6HNDRR0obT2BgoKaoO5QUVEKUpvYKl6DFNbj2Ha4saFN2jqPWL+57wyJjNpApKF+MEwj5nJ/Jn3v0m7FMVQSSyrvhT+rlghz4LRmILxhGPPbZLjVDnOSyGxze1dCmczjp1qlT7e3zjOS6aY3x+QP3jhjSGCk3Vu2+RUKnR+eU2NvXrcavH4hPvOTVs9aQFiJp7852h1bf1H2z88VrNRdNd7SM1jLAurGDbGBmA6DbklwdhrMOIea1sXV2rGjLUakRaA1KEQTMWAMaRSfFyEVQw+APgldO8f6eDohAsFsaCvyUSdcA7SsrG1w2kxeSRzaLpH+rwp5SAlJg8lzRYRIB5hTMf2rJD7C8K+qXRJnPQxDD9VZEGJzsFbyyn06pKrYEujVC/mYYUJY+lDEEJ4WPKPHptjU2yoC0ladY9NWO9ZUiwLEbN5JWSU/lhF8GLGLQnG9HVyXawo0RR4S7yt3kwe6Q2+ZrGiNFPIR9XvD8k7a3Lc7X1fZHyIcSL9Q+y5p/E6l+etKNGFwBe9EhEXpdDvGTzyB0OOG/Uan6wI//+ufoUSxYi+ANWxfhXY5qMWAAAAAElFTkSuQmCC'
        config_peque_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABMAAAASCAYAAAC5DOVpAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAF6SURBVDhPrZNfSsNAEMZH8d0XX4QmN1DQB8U/N1BQUBvsDSoiSlF6A0vVY5haPYZpeo4m3iPmm84s020SX/zBkGFnd3bm28lKUUL/RGOyZJJSkk7Z70RtCsOA/VqQrI6tnb1ifWOTDf5fLFQWj8YUj78oDALK8pwr6z/1KGy16ObugY6PDks7KNen/O0/9uSkwClL3uMPV4XaydmFRIviefi6FMeaxSXDQWwAs1nG5oO172TCX+zt3t5LZM6qFMhlA7QGoavExhpahQRVuGTQAUAvZfDyRqfnl7S9u8++YvcsgLL11ao0si9qNbJxlYR00RdTkwDVyB8P/6xr04d1k3bU93XMsh/xBNyqVdjX0VGpa1NfH3FIBXg0kBCJENT+8cVhHMIBm0jbthoDN2d+siY0mb0AmNFIxYMWOZsP1uw+HSeHJOVbcJu1Ko2sQVfLmuR0P208+qTOdZv9wXA+qPjRUZH90TvRVbkv4rhDki4BXexLwm+mKH4BKpmIg++NXgYAAAAASUVORK5CYII='
        explorar_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAYAAAAiwE4nAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANrSURBVEhL3ZRfSFNRHMfvvTPntP1x98/uXF5XFnrLkTrd+jPLVRoiFRn0kkF/oYdegqinHoLoNYge6qEehP5AJERZBhVEpGkFJmnNUqdLp3eG07ZubvPe7rmdoNv+uPXnpQ+M3+HzO4cvd5zzQ/57UFiTYjabl5SUss1fI7H6t573bqawEDGRpD83TzMwx4daH7S3n4db0yJlYM3G2uO9fZ6z0hLsy5LlL6xxOvjXr7pWTExMjEGVkqSBlY61rYNDQ42CiH6lCdxLm4iWWDQ6plKpstQ5OcsiUWFnb19/OdgLvpo06k49fvTwjHw4U+yONbd0+SZOh1OfXDUbjkEdh8ViKbJVOEQ9YRZB1el0BthKn6pqxwGdkQpocWq6yGploU4KCHXVbukBoa6N7hdQp48Wp4NaIx1iV650QLUgBQUWBgSC3/r1rj1QJwSDVaaUZRtRQYywJcXP3vb3d0O9IOPjY6Ory9iLYB0VkGZZJkERqNUZ5K9ahKEtssgAbmL8MiIIc8FgkIEqIYrA6eBsA4KKKACqtPH5fO8EVOT9kwGr0WgkoI5DEchxU1YRxdTDw0NPoUqbcDgcoknKK700kaIoK9RxKAIpEh/FUFRLkskPpGIywDHSy573+/2DUMWhCNQb9D5Q6YKCBllkgN1etQNUFBFiMzMz07JMgCIwT6PukBeY6qhcMyBbrS4URSx7eXHxE6gW5uf3VF+/NaNQaTJNSpNpymaz1UGVHvsOHGwDgWBUgSkCdUoqKh1XQWB5leM6VElR/KWAl91dp8AwHvX5ECNl8W6odZ+ArYQsL1nVPTg8shlVYYQKQd5AnRRpjxKO4/xrnVUDAoLtAqGT3FRdWZmtvIhhcJ7/8pHn+VC103mYKVq6ezY0dzUc/vJ9YKNCBMNUBE2bAlOBgEd2CUj4wLMkmpqa9ubj5P4bN1trJBUV54Xg964C6c0RIxH+8yGcoE9+8I5uN5lIr2Gx5tzLF91X4B4FKSeKWsLt3nQkEhMqZ2c/53sGP7ikAyJJkF4TiT+Zj0U9Xc87L8HtSIW9+trQyMfdFtocNOhzT3d2PLsgSsD230ej0eTanetu/7h0LMtW/86YzAi9Xp+/tWFb8Efo3bZ7n2BLJu6W/ilgyjy4f8cAbjrDFCI56uwe2Pr3ZEvAJQRBvgGc/iT8lYhktgAAAABJRU5ErkJggg=='
        flechita_inversa_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABUAAAAWCAYAAAAvg9c4AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADRSURBVEhLY/wPBAxUBkxQmqpgGBv66u07KAs3IMnQqzfvMDR0T2OYOn85VAQ7INpQkIFT568Au9TByhQqigOAkhQhcOXG7f/BKYVg/PLNW6gobkDQUFINBAG8hsIMrOueSrSBIIDTUHINBAGcEfXq7Xsw/foN4SSEAaCGYwUw12aWN1PH+zAAMoxUgwmmUzFhIYZpHTVgNijhE5OjiC76QIaBDAWB7MQIBm11FTAbGyA6R4Fc3FCaBWYfOHYaTOMCJBfSIBeDLMAHRkt+agMGBgAyIBcEgb+fDwAAAABJRU5ErkJggg=='
        flechita_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABUAAAAWCAYAAAAvg9c4AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADWSURBVEhLY/wPBAxUBkxQmqpgGBn66u07KIt4gNfQqfOXMzR0TyPZYLyGOliZgmlSDSaYpECGgQwFgYbSLAYxYSEwGx8gGKYgQ0CGgUBWRQtxLga5lBjw8s3b/5nlzf+DUwr/X7lxGyqKHZCUo2BBAaKzEyMZHKFhjg5ITqeiIpAwFRMWBNNYAdi9RACQ9+u6pxLlfaIMBRkIMowYA0GAoKGkGggCeCPq6s07DPU908DJKjsxgkFbXQUqgx/gjagDx06TbCAIEJWjiMlFyGC05Kc2YGAAAI1LhoZCP97SAAAAAElFTkSuQmCC'
        hitler_encripted = 'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAjCAMAAAC0CkrjAAAAgVBMVEUJCQmBgYF3d3eXl5cPDw8LCwtwcHAFBQUCAgIMDAyKioqOjo4VFRVkZGSRkZGurq5VVVWUlJScnJyqqqpLS0uzs7NpaWleXl6GhoakpKRBQUGgoKB8fHy2trYfHx+6urozMzPW1tbr6+vi4uLAwMDNzc0mJibFxcUsLCzz8/P9/f12W4ygAAACqUlEQVQ4y01T6darKgxlEhQBGRzAua229rz/A97gd4ab1R9dbrKT7J2gCgmBIMpSqGvcV4WqsiqLEv0LARhS79Hqod3XFcF7Ud1x54oSsXUciPTeYduugomC3QEwBKTu2nWfB0Rww8WE+gMDsSgA7sPj9fx+fz1fC1mr/8NIMPW2/ny9fh58WvWXvMzFC3VZk7mf+cEzvtGf1m6YrXs7h207X8/X4/VddlbcAQPn33qNNnZbF7YlpGNbBpYHLipUQvFK7Xbo62ZpvDdGNlO0tx6QLaqyZJfmnLjUQWpI6QjYsh/81qQc65mQWE/L8TmPx3mG9i85cJd77eRMZpm6zwnVH8dYAXEBnUMuiGYpJZxE6sPitXV+VFUFKEOQWxZi1UT3RAIc5vGy/GKQnmFxy8beY6tJdFMXettaoorqN3n5z01Su+ANjlIr6BlEK34cE+9R97odZmz8NCXfKvHDnrdECDZGjLm1gyYmLdu0qxLkRtVvv1fdhVTzoW2HHtc1V9X9ucjTC6H23n8+2yT5YK1txwu0vCXNK1iyvdV8Arc/DUyvLyUKgIvcGRLQ9NBzztP5fL7OZqqvKlt8a14hADkITvhMH7AIj2a6GAOfcldgCVghJZlxnGU4v98zOatYmSsXmWKi3gA8x9pE/3ge0mA4BnYvNzS+pMlE4MbSRNmA1XXCvIdryJcgUOOpMZjoGUtnHKXYhTQlivtxLUSBAnUGdAa/MI7wEBsaQupCR/UbxvMyYkdrbmGfsHMxSjI1Ke+kaZlAkvAeMqTWOtd3VPZug5UNzdS/BYI+Bi49lfCH49r7mpvlaLquSRE2bgYj+rlOEwUeoPcU18vRbUsXpqGC7KEdOKaeOolhekpjhhe4hdArFIlurSbwGY5bSglt1N2xLJ9j67j6D+qFO4G5hsGIAAAAAElFTkSuQmCC'
        home_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAYAAAAiwE4nAAAACXBIWXMAAA7DAAAOwwHHb6hkAAADKUlEQVR4Xt2W3UsUYRTGd00t7UOiggrdJUqIICGjJNekuumiD4Mka73tJokoTFG66S6/iogg/ANa3fQiyyCKLjIVLOqikkT8aGezSEIWLKUvp9+xeWWaeVd3666Fh5k57znPc86Z876zHk+SP9M0U0FGJGIUcl2UZHjy7k+6e/YeKDlqChDNRdSbPEuCEadOn92ctXrdBzABJsE4tsYEw5Nz27ptZxkCfSBCdS0CS3yMta6boda1yTHO4w1xPzAg7qWlq5QrInnYulkbA+9I4to/iUJyHwyB97SuPh4Za0GEO/AbBAN/JUrgKxAl6zBVbUqEBNFmYt6IKHGHFowh00ycu8BTaeGlhqaKBYM0Dgi3iaiIx423WhLBaQSMIlbqdLZvAbbEvNvB4hnmOgx3i+JKsZGm+3JyRsE4tkxfdvZ3u6Bs+FBL+CLBJiRm3vYC2RYfGZz1caqYgWsQ9Pt8Oc/iVkrv2yGKQVSunBBL4fmxCDkQE1G6scNJKAMEl2vQ7BWqmHRussBiO0nFmXPF8lwUKPS8fN63pfN2+/7g8bK7mLx1DZc7NRX8wBZz2lM1jq4kDCO6UfkhtJT7ado0QLuGunt6A0Y0ukzD8xPblNOuq/Cr5WQqZwg3zN0b0T1er9cUYEuz1nSJa1+bTlCGRTL7piJ2FwUeUM3sYyh86x4Tuk++GHWNV9QmX6lhlyRc/DpBEfosbbOTBE8ca5Jn3peHCX2Ul18wFWoNz7rUVFfqTiHZNq7KdYLSKsFchUJaW32+SoZEVUorldhkTVXlBU2FMnwrnPZ4QyPZzTidb1y/eph2+hHLZ5BKmNhmhueF05ctVMxUy5S7viA6wQwcFVyJ+/2+CMYI77BDFhkeV2KY5YWngbkviyLStXQJi8utAE2nfptESInJkWeDcGaCNSDf+Y/AVSHv6K0QhsJtJ2nNBLcj4JOVhM9qkxBK9rJdsjnyvlg+Ma7TxDYIR1Fg1x1nxq4DmE9R7sEjpa9xlFZNAjVEcpXsJUaG4Y+TSNcKTiQ/r8Cwr2lPfPn+scfqGQy/5axEVazEKdj5Zg8LhukhA1arS+L/t/0CxAJAk5AIk/kAAAAASUVORK5CYII='
        kkk_encripted = 'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAjCAMAAAC0CkrjAAACOnpUWHRSYXcgcHJvZmlsZSB0eXBlIHhtcAAAWIXVmE1ypDAMhfc6xRzBSLYEx3GDvUvVLOf48wTpdNPppAlM1RhcxY8tPeuTpQ305+03/cLFKkYySrXegnYqetFkkYOyJjUdtMjEVurlcqlsmB80+kwySXGSECcLUWDb60Cxt2xwTGI5lhQhniEoAic2qVLCFLKM1ku2XuGqk2+nHQf/1lGLiWSCwcSMeKJWj0TysvBhXpmlQIhhoZITxxh1LeJrhEUX6i1iBMlwrDZfXAxWXLTC0LhKJ4MPvAVh3Bn3admAJzIx5ML3tp4n38HX72NAAEgKkFkHC7AcEHtBTO/roGGthMx5Aj2DaU5mVsWSSlI3jJIgD3QR5GxCVJ6EDnN4ioi/+VMID5wBDHphuEMd1yoDcJQn+AFbs45XdOLqhrgnOCZPsYMCEDnhInOy8f4SlR5Z96LSI+teVHpk3YLqoLNcngETThx1BPdVwaHkrftccK/qjbYW3Kt6I4Q36iAl4q7oTBiyDWjQCndvSZyImgNASmTk+nE4s991hm44S3uGwYcvP2bhmoSb1H0h0K0S1kZLc77Pfer8ZVMOt0H3H0fG/xFaw7QQ0QGh72BOh7Yd5gRoe2FaRLtnaSOiA0JfH8wJ0bZW2SnQ9rVMo2j/ov9bQbuxtBLRAaGvDuaUaNuq7CRoe1qmWbTj/d8O2pWlnYgOCD0/mJOibamy06D9vGUaRjva/y2hLSy7hJ79uyT/rbP8pjRb/jvSX95pME6WV0wkAAAACXBIWXMAAAsSAAALEgHS3X78AAAAh1BMVEXe3t7x8fE1NTXo6OggICDh4eEoKCgwMDAaGhrr6+skJCQsLCzv7+/t7e0+Pj7V1dXl5eXNzc1DQ0P09PTa2tr29vZISEgVFRU5OTk7Ozu+vr5YWFj4+PjS0tLGxsb7+/utra0PDw+1tbWMjIyVlZVQUFCenp7///+mpqZnZ2dhYWFzc3N/f3/T6dvhAAAC5UlEQVQ4yx1Ui7KrIAyMAgrylviu1lZtbXv+//tuvNEZZthlSSAL6LzMB93Wed7nus6d64e67wd3RdtCUVS6mL5VUeqqLOinKItcl/8DuCx4/yk5r7jUsuJVQR/XvCiIoQnmct8f/BqJI10hK6lJs6qIAB3nLc7tBUrJu2Mb9H/epVERLIsX4ushpXxw2Z1/D95xeXwkMXQORdfOCIuWsntUMp834km+rZWUFYnTYiGU+CsJl3JaxFeWvI12yiUvc5BHVIElNk5VJcsds2dxFD8Mi9OlI1jvs0gqKK/74/O0wrfT78mC/fFpciD5HkPApPC1PdcRs7ROfwAqxamdKpD5guL5BCPm78d7GKPZXgGVzeat5vBoPapxRNbM5dejfz0hClAipBQ1wd8oMhMaY8X0isgiwhhQ4B6t+Uh4/HnPkjKCmfMlkHIKowAM55jS1kG3YbTpplTIMM6gLFsgi0RXVo0lFCsDo5pMMQUBGQvGB0o8Y0w00YFeBEvpnozF3XtLBxQV7dAYE+6+htIjs9nNWBXOAEwldSWe2aCY9QO4BTOCrUpNjEHQ7BxAKaGUCeqAfMNks6SWsPx+IoTMjxjokpQNIW3QTWhslqlR7I8vzTfzekawSSQQ4wceB5h0b27N/dVtCTGFcRuBKrnbsGs6NWSqSe93OqvtJkKWidODsYylbHQkPgeTmvv7dvbrm2FifqVbiMJSDQQfM1Vze9/fT7c2wmY2roi4CmUUTiDdzEgx3e9jvbxRhfuyzh53YCGEP5CDZ+LWNLc09qfwJqnXGmf/AxWEWeFRY0BLkfzgjuP3+x5Pvywf0qGGo3ZApRqTUoZTSa1dFPU5+0hdwIRA6IbXusRxmZ972+dlmXN+/J3ntMwQ1x2qrpDO6ZyiHPK8dlqX+eXR+vNpySWanFuRn3RPDneDI3P3l3d12Tu60DInT2td0NqhJ88Pl/WH6xlwdQ2XKsmRnuvdUF+PQt1eUV/DP3o1Qp0eZQH+AAAAAElFTkSuQmCC'
        listas_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAYAAAAiwE4nAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANVSURBVEhL5ZbLaxNBHMdnZptH82iT3c2j2tomBGp9Va3WB0q9e5C20KPgQcSjBw/i41/w5kkQCmo9CR4VLAh6slWroCgIpZWaVNM86iZmX/5+4yTGbuJjPfpJJt/d787Od2YzmQwlv4ABFLAB1I2IagSvWwAeoyL8QgtaBiqKEtu+c9epleynk5DGmNQRYpKkSpLUKaq0Ra/VllQ5cvfJ40fnWgW3DOyKJlZAYFjwJsQLHx0wXl6XEssgNrywAiUS+FA4NrXsGtyjw9h9xKJmaS2bENfaM7Jv9CIEfhzaMXxVWH9Nb1//ybCSLCSSPYeE1YAJbQBf1jDq61cvznHDBctLi9PUtnRZjU8Jq4EjkFAGj49Q+L5Q/wmJMZ84bOAIhEpeEJpKpUa+Oy6h0HVKPeKsgSPQ4/FEqMRi0ai8WViugMntI9KfBPp8cVS/3x/iBhCPx9MwCYrdao/ZothhOVmGjvpF9TpUItLvA30+fxI1EAh0cwPQNC0fV5U3qiI/xRJT5LmYLM/H5OgzOJ+Px5S3g4Nbj4jqJJPJHIAlI8g62MZOODl+YtLGXk9MTF4R1l9z8OChKWxj9PDRB8Jq4JylAllR+sQhESsZB5c7BGbxT6AnqsNT8gVRQ+HQEDeaaBs4MDCwBwOwsfHxictdStLCEpYTJpZQNG40lzNnz07XQxVV3YLa6Q84Jl7bwFQqPcKHBKTTmVFhtyX/Ob+EizgeG4ZR42YL2gYiuPjCzcb09I3T/Zti+7H0qN27YpHgtkjQmwl4SF/QS7eg3pm5faEeWNG0Im/gT6hPmpu3ZvjNbhgbO3YK28C2hNXglyN0S6VaKaOWCoXn3GjCEQhPsIL6cmHhPjdcUCwWs6hftPV33GjCEQi9W0SdnX14nRsu+Fqtrlu2uQZTwDF5HIFfK5Ul1FK5tMoNF+RyuffUolXTNDVhNXAEwv/YHKppsWvccEFmcIj/eZcKa/e40UTrLYac0CBZg22CAfsGg1ikYtlWCXYWa8S2yrAsd2E9asMWg9EoIzRgM+KFxsR2AzdYtl3Or/Z+P/9By0Bk996R8+VyZdyybR1+Xjo0YIDWYH9WtUxzHR5X3jD0VV2vfTB0I8ckFvJ6/WlYmCLZleVLopn/DkK+AWbaOqQAQouLAAAAAElFTkSuQmCC'
        more_options_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAO+SURBVEhL3ZZLbBNHGMd3ZteO7X141/GubfyKYyhOiRHGNIgEUQwFiV4rkKh6KJVQL0hVxQGJI+JY9dATFxAnxAVRVYgD4oAqHlKgDZQkLW1QSngojjeuHzhx7Ky332wG6BJDgrn1Z61mvm/m2/88vtkx878D0XJFEEKCy+XKQLVqGMY48ZnAi3IRIPU3saIQCDgdDkcfiOQ8Hs9+X7fqeTKdjwUDgVmQaYQC6s+N+vy18fGxK5VKpUTDlvFWISrSL8vyCRDa3Wq1Zqv1JmcaDGawiRmT/JA1K031P5Jl/tSd4eHTVvBrvEmIxRh7OI6LK4ryPYhlQOSfWq12hheEa9BY1HX9SSqVyrk8ws6FRrNnYmJyBwlUNf/fDx+MbbXeshIg0u31eo8TkUgkMq2q6k+wbAdpc1u2fDTwlaQE8uRZu37DMHW3hy7VelEUj0Sj0TKIPNM07RLMLEGal3q9neS6D2+C2PTGzdmz1LUcmAloiIeDweDtcDjyDGZ1FER6SNNSj9UhKNqk4FOnREkKUddyJEW979eCozzPH4AZitT9zoiy+me8d+1FatqJRKP9ok97Guvp/Zq6OkbVAntFxf8HNe1LEosnDiETITiBj6mrYwoz+SuwrcaaNWErG21C+cLs9hZqGVOPJi9T13tiYqdbOE5qNqGZwkwYDmCTmhZuSbkQCse+o6aFIKu/iYo6Rk0LQfbf4r3dI9S0MEEHEsxF6jYhOOIGrb6EY7lUda7+GTWXwEgyEWNLFMQgP2JZhZpLYNOp68UUtV6xIb3pB0jL994fQigU+oCcp+zANivzbDNqGc2rMDKc2Zz9gro6Jt7TewgKLHulKiwftglVyqUxyDq2+rz+DXV1jD5b+gSxWO1ycHfhPCL7HpkMSQQ8U9DjuV27rWzphG2DQ0cKxeIWUh8dvf8j3F/2vSfKg0NDn3v9ocW+dLbUn04P0qZ3QvIF5uAdJgz2MHUth4jt2vPpFOmYzgyY8NXmadOq2JjJnoHY5tCO3C3qsmj7RU4mkym9PPc7qceiUcaBW1+O/PrLeRgDD7d2HUoOmlioz5MS6Ib7qsxLvmETIzf4zOfFQpzEv6CtEJlVIpFY15fOPLh+46blEz1dFyul4nVY7gK8WIEu7mazOUHE3W73noXGYsFgUHKhVjkIfeasoP+w4h3z8c7csZF749+yLJrv4pg8JCo5lC14SOwi/V/yV7lcPtloNO6RmHas6jIjOJ3OLIx8X71ev8pgNuER5XO1kr6JNjtA7CG57qn9GgzzL7AwNw7InubpAAAAAElFTkSuQmCC'
        msg_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANXSURBVEhL7ZZLTBNBGMdnZtttYWlpaSmPosESohgrIA8FAY0HNUZNBOPRu8SDiQSVg2cTLx70gAcTYzx4MEYvxsSD8ZWYKIkJPlaKPLQIpbSQ7WOX7sNvl7HpBppohRu/tDv/+fbr/nd2Z74p2mS9wbTNsqel5VC1f+vgfDRKJEmMyLIsIE1TESYWgjGD4UtTDQgmLGGIDRNswYhYoSUMwxQ7SrjIGP9laGJiYoymGqwydJRVJCGsYayKGiIsmJkM4AdYQwg+Rk+XmICvcYogrKo4QwjmVs4jVOlxBnmeH6VdM7sbG884Pb6FlvZ9D7ds2Rqk4X+CZdmipqbmY8Hmdq3UW6WdO3+B3twaBOobXoBhNBAItNJQwbS2tZ3SDXVjeA3ZJ6k/iiyqqiSRiuWZmZmvNFQwyWQyTqUJk6GmIUVvRFFMrEQKJ51KLVGJ8o6QEGTDDPE53RW/cpMKIbaUfkZlfkOEGDscCJhWOt2+tMPlC63E/55ip/uJPg9o14AAVJoN4T5YVVMW6wK1j7zl3o+IaHYY7SxX6hnBhFhp2prYOecw5H0ghKn2uN0jwV077tNT+Q1hzcLiZlycnX08zn/aK8Tma8q9rhuwropKXL5YSVn5VF399ks0HVVW+/v0m9FfAWNhaottlqHEYrR1IsQfzkjia5pmwmSo6UsXqPH7dxoBYHyMvybEow1Oju2HBCWysHjVUVYplHorpJSUua2PPCMJTcml+JH5yFz2vdntdgeVSAGoNBtarJYKvT1+4uSgEcgh/GP6XiIeCbgdRac97tI3iqLN+Mpc/Yn4fBBm5BxNy1LMcS4qTZgMWavNT2Vepqcmn06O80fBfFto7NsDGl4FlF+VStCw4Cgmw/VEEATTTP3DhhmKaVGg0sSGGeaWtryPVIViSuV/A0svu63lGprKV8f+7uuf+dBA1/5O1NO5d/Tlq5d3Ywuxn9KylJIzspQ7EfR6pV9JhQ+GDmzUy6KYFmZn50KZzLLY3tH1/PPXbz2XBy+iK4MDWZ9V9VLfUqhcF+4M33rT19fbRburDXW6Dxy8abNxvYjB1lQi+V2WMzFFkVMwQBkGpUABWLkp+GNgbHb6AUoUXMy4HlQdR1VVtf39u7dnw+HwlJG7ySaFgdBvyvM+VA79KIsAAAAASUVORK5CYII='
        notifications_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAYAAAAiwE4nAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAMFSURBVEhL3ZVLTBNBGMd3W9pt6dItbaF1aZu0UKi22Ehti1BeiSAJCWKQxMhVrybGxHjmRExMPBhvHjUGUSHRxJORIMbEEOIrEHlsKURAoQ2vslv6cGc6HJaWlq0X4y+Z/L/5z7f5ZnZ2ZrH/HhxpTmi6wmKz2ZrlCoWVZWOdGI6nCLl8Nr7PvWMW5seWl5eDKDUveQt6/f7rP+ZDD/mwKO0IoWljREuRAxPj4/eRlZOcBT3e+uE5ZrGXD/f1Ou2UWqV4kEwm46srK59ok/ny1k60b30jXAdydaWasYXZ6VYQF4THd+4lpT+RKtEZt5wu1yVkZ0VdalgDuVZbVc68Iwk0Nd+ExbTGHWTl5aAo6h6JBKmAX+vha7wkDLqSnrSTn63ImgGoxWYfgcZx8fvr+8BMwYyRdWxIbVmIfzaOulnJWKGMUDQBPemoegQNESTZaAsvUjVFVaSdTDIKclzMCnQzEn4DDRFEo7sMUP7Y3oBGFjIKbm/v1gKVFkll0CgAluVOoTA/YP9AIwhCgSxRoP1fRd0MBCukadqMQv7VciwKRZFKJvdSOE6ibgaCgjU1jgsoLBhjeVlQIsHlbrcbfnyHERSUSKXwvvT5zkagUQCUhlrgRUZRmsq0I0RQUEWSTqBKgviC80BTJOoSyg209Xx71stc8AdIJLFqoEww1NLd0/uWi3Gbif0EG0/E9/j6EmWxspxj2TCWSsErDPgxLrYpkxNqklRV8MVs36ZnTGBscnKKAnoYwSoaAi0T32d+NKDuXxFobMBejz7PeEsCw2Q2u5yu2n7wC+IHcBmh9L7/8LEDjHnrTg9YbZWtFovFt/F7fY6i1CZFcbFm8O49+Oyd27egHmAxmbD+q1fEbYterzfUnvHBc9nR2TWEbIiTp+tiLxwDbZAHDeUk7wzqPJ7u+cWfoyC2mM1YW1vga5m+3DH07IUstLQEc16NDGNNgUZxq8mF3V7dfrCSw+3xk6cpGQ9KzYuoWdlrHP1KpaqNP64kpVZ9XgwywwzDzKLhfxEM+wPxPeq9+XXcCgAAAABJRU5ErkJggg=='
        profile_big_encripted = 'iVBORw0KGgoAAAANSUhEUgAAACMAAAAoCAMAAABDwLOoAAAAIGNIUk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAADnUExURa+4vq63vbG5v7nBxsHIzsTL0LrBx9LY3OTo6+zv8u7x9MDHzOLl6fP1+PX3+rvDyOTn6/T2+bK7wdjc4cHIzezv8/X2+bC5v9LX3LO8wt3i5ra+xOPn6+To7LW9w+Hl6bG6wNfd4cnP1PHz9rjAxePn6sfO0rK7wM/V2rO7wcrQ1eXo7LrCx9bb39ne4sPKz87U2Nbc4Nje4r/HzNTa3ubq7e/y9fL0+Oru8fX3+b/Gy+Dk6PL1+LzDydzg5LC5vszT1/Dz9s/V2ePm6sPJz6+5vtDW2tvf47a+w7jAxufq7uns7/////XZPbMAAAABYktHREz3bxDzAAAAB3RJTUUH5wkIFRI0TJwu+QAAAVFJREFUOMvN02mfgVAUBvCSUeJeriVLhigiGQwh+75+/+8zk0Hh3F7P8/r/6zydUwzzv8M68RcBLvgR5AJ+KsQLYTEs8CE6iUQRdoKiERqJxck98RhMEkniJpkA+6bS0oNI6RTUO5NFnuegbAYwuTz2GJzPAaPkwpMpyCxgPp+MAJli6cmUikBppUy8KSvQy1dUD1Er4A61qjsMVzV40TXxjrBYo9xLr98QFus67agNo6kSTNSm0WDoMY3WV8swfYSitTvd726nrSkwYPVe3xoMEULDgdXv6dDdOX5E7Nt72WTEc+9kPJk+3WI6Gb+SSJO8pvnyUc8E8h5h5iXynECZyy5ZLFegWS0X7uYsDBpsudtcIwIHrR9tNphi8ObWiN2KEsVI4vZv3bs9bdTvsP3uahIHm2rsw/WfZo/UOk6hozOMPZ19zPl0NebFx1xMlvkBCSY6i4zNmg8AAAAldEVYdGRhdGU6Y3JlYXRlADIwMjMtMDktMDhUMjE6MTc6NTUrMDA6MDCdxjFyAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIzLTA5LTA4VDIxOjE3OjU1KzAwOjAw7JuJzgAAACh0RVh0ZGF0ZTp0aW1lc3RhbXAAMjAyMy0wOS0wOFQyMToxODo1MiswMDowMI8izRIAAAAASUVORK5CYII='
        profile_uno_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAJySURBVEhLvZVLaxNRFMfPuZNHm5igFhVDKVpcxtiWCJWupCvBlTQihZgwwWJwpd8gX0DcSCEu+kCC4AcQd+1CEITUZlEQCq1S8IFiIT4y6cw9nkkPRZlMEkrqD8I9/3Mn58/ce+4d+B+gjF0hIszn82eCWsdxYKCeSCQ+l0olLdMd6WriFjfN29MK1HUiGJI0IOJ3DfrFyMj5l93MOppkMhkjfixyj4tflpQXBbVAIPyoXC7vScaDkrEt8Wj0RkcDFw0p27JuiWqLr4lpmjECuiayMwqmC4XCSVEefE3QcVI8BPdVFwgMsu1xUR78TZQ6K2GvnJLRg68Jd5UlYU9wtzUl9OC/8Y6zKVFPkONsSejB12R4dPQdb/xHkV2gr/VGoybCgyGjh9XVVUqnU++B1BRL/zfmJtagHlcqlU+iPfiauFSrtW9j48ltXvEUAoYk/Rf0CxTNLywsv5VEWzqa3J+ZGZyvPNtJJi+uGAH1A4itEPYQaIffbcVqOk+Wl59uuc+93tiw5W8e2l4ruVzuOLtnuNAUadjmh96AYWyGw40v9bpqxmI6ZFkDp7k7Lrg3As+f45P/ygF4vrS0tCtlDvCY8E07oZDm+IBFJdU7CD81YXlxcbEqmRb/LBfftlcVYJEN2qx/T4QU4uT4RGp3bW2d93KfAxPTzKaRjLvu1S6pw4IEaiydvvShWl1vHYFWaxaLsydA450+GLRArqNtmpud5bpMy6T5O3STpyJu3D8wMhhy63KUzWaHgoZ6yHGnA3c4EBxUgQcqGFSTLPtv4OJ+Asi+okBTUlJHA9fnjsVhkUcD13eXKcbfAjqqHwDE/gAggd2dx830LAAAAABJRU5ErkJggg=='
        saves_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAZCAYAAAArK+5dAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANjSURBVEhLtZbbSxRRHMfnvjPO7uzOqqOrKaYiLhVhaIaJRUoUURIZSCL1GvjQQ75HRQ9B9Af0IIEE0YV6qJeCELyDFEZG99JSdMvLmuuuuzPT+Z09O+44GrtBH1h+5/c9M/s9l985u9T/hiYRw7JsqaYVtMYTCe1naO4Sx3HFhmEsk+6NmKRPT6abYzPw5gVM3YjP0zodp2hjzuuW1EQi8QV9kYm6w8mnksCXRyLRFZNm6zhOKFQ88scf3782km4Ly8Dvzz2tM0yvx+19E14IXVsOh1/IsnyOYRgBdTtGaZpmOBaLffAoSqmaq10N/VooClaV3xkeHOggj9jZXl5xU/bnzxcGAl1EypiKysrLMPvzXRdgprZVYUiEERmMYSbWYmtLRMoYtIxR0nRgM4Co6/qWD28FemcN4moksoqFNCwDNC88NbLmWZEyiEZXHBW3bsCwnMlQrCAICpEyBhnEIK6uxLY2YFiaYxnezwu8TKSM0ckeoKr9jYU0LAOO4yWILMu5sJAFqHSgeqh4LB7BQhqWgSjl+CAKAp+DhSxA+8ZDTJiG47xYBorbUwDRJbjcWMiClAFt4hNvwzLw5aoBiKIoZb3JyICDqJsmzMBmYhkU5mvbIMqKR8VCFqBLUYRooFsSC2msb7Ig4vr3KoofCxtAowygTyFJbfC8gCuPZmnbNQFYBim8infjDGifz3fU4y+Y3rG7dqY6GLwOWrIriegS8bJyLOc4pCkD64Wi4uIS0gTYtvb2UZOTnkIyOTVFzYQWu+vq63tQag1OlFzYwCWKjjPkmIFPVb0QJUnac6z1VOLZ875ayBv3N1AnTxzHd837T5Nnd9Xs1Xmer4JcknJw5THoEKFgm53DAAgGg92C7BvrHxjEefPBxpEnjx8wt3tuFVdXlvWCBrOp3lnz7sCh5kcMm6wigePxZqfjMOgfGKKmQ4uwzlRpSQklskb7w/v39qEUXbjmwsjwUOfKYqgC+sDk1fhE69JytA2edyseR4FsYpAcNSzJ65ej3Ozs7F0spIHu/88T42NlRZp6A3IwAlQ1Nw830kgZ2A5HU0NdH1oSFjW3/EFHN+i3txMTF/N88hUi/Z2Ww0fG0MaZiqK0EClj0L+REni3/UzHLEodZwGjaVonaf4zstvdRJoEivoDTzMUlOdM4HAAAAAASUVORK5CYII='
        stalin_encripted = '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'
        
        #desencriptar
        verification_decoded = base64.b64decode(verification_encripted)
        captura_perfil_decoded = base64.b64decode(captura_perfil_encripted)
        config_grande_decoded = base64.b64decode(config_grande_encripted)
        config_peque_decoded = base64.b64decode(config_peque_encripted)
        explorar_decoded = base64.b64decode(explorar_encripted)
        flechita_decoded = base64.b64decode(flechita_encripted)
        flechita_inversa_decoded = base64.b64decode(flechita_inversa_encripted)
        hitler_decoded = base64.b64decode(hitler_encripted)
        home_decoded = base64.b64decode(home_encripted)
        kkk_decoded = base64.b64decode(kkk_encripted)
        listas_decoded = base64.b64decode(listas_encripted)
        more_options_decoded = base64.b64decode(more_options_encripted)
        msg_decoded = base64.b64decode(msg_encripted)
        notifications_decoded = base64.b64decode(notifications_encripted)
        profile_big_decoded = base64.b64decode(profile_big_encripted)
        profile_uno_decoded = base64.b64decode(profile_uno_encripted)
        saves_decoded = base64.b64decode(saves_encripted)
        stalin_decoded = base64.b64decode(stalin_encripted)
        #convert to bytes string
        verification_bytes = io.BytesIO(verification_decoded)
        captura_perfil_bytes = io.BytesIO(captura_perfil_decoded)
        config_grande_bytes = io.BytesIO(config_grande_decoded)
        config_peque_bytes = io.BytesIO(config_peque_decoded)
        explorar_bytes = io.BytesIO(explorar_decoded)
        flechita_bytes = io.BytesIO(flechita_decoded)
        flechita_inversa_bytes = io.BytesIO(flechita_inversa_decoded)
        hitler_bytes = io.BytesIO(hitler_decoded)
        home_bytes = io.BytesIO(home_decoded)
        kkk_bytes = io.BytesIO(kkk_decoded)
        listas_bytes = io.BytesIO(listas_decoded)
        more_options_bytes = io.BytesIO(more_options_decoded)
        msg_bytes = io.BytesIO(msg_decoded)
        notifications_bytes = io.BytesIO(notifications_decoded)
        profile_big_bytes = io.BytesIO(profile_big_decoded)
        profile_uno_bytes = io.BytesIO(profile_uno_decoded)
        saves_bytes = io.BytesIO(saves_decoded)
        stalin_bytes = io.BytesIO(stalin_decoded)
        #convert bytes to pillow img
        verification_pil = Image.open(verification_bytes)
        captura_perfil_pil = Image.open(captura_perfil_bytes)
        config_grande_pil = Image.open(config_grande_bytes)
        config_peque_pil = Image.open(config_peque_bytes)
        explorar_pil = Image.open(explorar_bytes)
        flechita_pil = Image.open(flechita_bytes)
        flechita_inversa_pil = Image.open(flechita_inversa_bytes)
        hitler_pil = Image.open(hitler_bytes)
        home_pil = Image.open(home_bytes)
        kkk_pil = Image.open(kkk_bytes)
        listas_pil = Image.open(listas_bytes)
        more_options_pil = Image.open(more_options_bytes)
        msg_pil = Image.open(msg_bytes)
        notifications_pil = Image.open(notifications_bytes)
        profile_big_pil = Image.open(profile_big_bytes)
        profile_uno_pil = Image.open(profile_uno_bytes)
        saves_pil = Image.open(saves_bytes)
        stalin_pil = Image.open(stalin_bytes)
        #convert pil img to tkinter img
        


        verification_tk = ImageTk.PhotoImage(verification_pil)
        captura_perfil_tk = ImageTk.PhotoImage(captura_perfil_pil)
        config_grande_tk = ImageTk.PhotoImage(config_grande_pil)
        config_peque_tk = ImageTk.PhotoImage(config_peque_pil)
        explorar_tk = ImageTk.PhotoImage(explorar_pil)
        flechita_tk = ImageTk.PhotoImage(flechita_pil)
        flechita_inversa_tk = ImageTk.PhotoImage(flechita_inversa_pil)
        hitler_tk = ImageTk.PhotoImage(hitler_pil)
        home_tk = ImageTk.PhotoImage(home_pil)
        kkk_tk = ImageTk.PhotoImage(kkk_pil)
        listas_tk = ImageTk.PhotoImage(listas_pil)
        more_options_tk = ImageTk.PhotoImage(more_options_pil)
        msg_tk = ImageTk.PhotoImage(msg_pil)
        notifications_tk = ImageTk.PhotoImage(notifications_pil)
        profile_big_tk = ImageTk.PhotoImage(profile_big_pil)
        profile_uno_tk = ImageTk.PhotoImage(profile_uno_pil)
        saves_tk = ImageTk.PhotoImage(saves_pil)
        stalin_tk = ImageTk.PhotoImage(stalin_pil)
        #global variables
        #images encripted in base64
        verification_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAOnSURBVEhL3ZVfSFNRHMfvnc5ZzTa9c9Kc081d1oqam1uwZanbbKX9gYKyICqIgt4i+kNBUI+RRU9FQUFB9FBGL0FB9NJDhcLSVv5ZTrf5bzbNrGwjdzu/228XF9dl4EP0gcPvd77n3PO758/vHOq/g0abFbPZ7FgsV5zsDYZqilVM35Ili951+NsPYvO8yBpIoynVMQxTNhAdfUiqKSgczXEcxaVURUzX6ODAzunp6Qm+899SWlpa7t2w6a5CtYyDsrSwJEbKqMVqv4VdeORK9Qd5oTokLyoOFxSpB63VjlPYJErGjDQaTdnXJBfGKg83kxozVJY/87e93o0Sj7ygwEzn5t+nOFrGSbg8CSeRqtWqyLepiR1DQ0MR7CZOvWdjEGaxyrqGs1qtdSqVqiSXgM1ZMbDLn8PM19e5r9IElMVJL1d1td2D0l9BAo3A92KBJGgziEYj79FdMIRAlqqqTehSer3egm5WlioLt6M7G65x85YWCQHrPEKlPzr6GKyurIz64xoT5MrijhSde16r099EiYIcI4YOR0eO2h2Oht+DUUbW1Axr27RtBze7ca6A5Xr2ETnafboK4z2UBGrrPNfSY+URUP41o9jHT1fAziS+7UsRwM8huH1Nwx5vw1mop1m12notPvnJxigV/nB/sBllgfH42B2w4XDmCU//Pf/n0jypDCwc6abNW060tbWXtPnfnltfW3cc9Cqb/c5AZGgr6T4zEOoV2x9KoVDowYYjIoGMrOEFWK3OcB2C/CC87exs9dTW3AD9TaD7QqVp5au+UMSbolM/vozHKkAXY4bOOQJ2T/Mu8aVP5xAkKyQqaDqdzlDv8Z7Ba2gYrhu+8xzY1jhb0+PsP3AgY8kF3G7PoXQnlmVXoEzJZLJ803JzI2w+SnNCvk3B9z7fxr1FBJR5hBPW09P9FF2yR1IpulQikfje3fX+8ZeJmAGlbPBLNTX1eXCcwCuIECgajfajS1UaKx3ozhutVmtElwoEAu3oCgiBANhAgLw/N5xOZyOZvYoX5oGeNT0AC2NMEnhxFhmnwuVyuQM9oWdY5SHPRIxhFP5QsMeHEg9rMp8dGYsfJkMoSY4vRpma/hzPTyaTCawKZMzI7/e/tKxgfadOHEOFDJMjYeLxSYvVZj9Jcph/MqpsjtuxsfHTEkmOJh2kZq2Lmvw4TIsFmRO4FeAqIute4XS6+OtJrFy4eGlhb3mS7YXr6hs6YXDIM7jHWlouP8HmfwmK+gm3bT3BJIskEgAAAABJRU5ErkJggg=='
        captura_perfil_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAYAAAAiwE4nAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAL5SURBVEhL7ZXLTxNBHMd3Zlv63kJbti+aAqXlIaWVYBXSKPEAiUaPevIgMR704h/gX2CMF0+euOnNx4WTIT7ixUhCiIpSHsFSHm1pqWkL3XZnnF0HlNDQLcHEGD/JZPL7zi/z3ZmdmR/zzwNorwij0Xgdsw0XWZVqGGBgwAAXeVvzQmp95UIul0vTtONBp9NddjpdMxqNJgohVEdOn7lpsjpyZptTCPQE52ja8WG321+S9lar1UZJKO+M3+8PS6YmiyPfGwwOSVotIO1rIopitihUCqVS6T0JsaTFYrFp3madBwDtZDOZDUmrhWLDQnH7tYgYDcZYoBJZYWAwlUx7GAQqiURigcqHwtK+Jga9oQKA+obL7RpxOp15t7ulf2UtPQ5YprHN63m2sb76gqYeSl2n1OvrnMhmtgaIiVmKschkrFbL3NL87Dk5QQF1GUr0hUJXIKu+hBAura3G76eSyS906O9E8QoHTkXGBEEoMBCOLC7HR5otTZ8xAgiJwsNvy0sTNK0migz7I4NP52OLUQyxmhxsCBAuyAMQN2AMtQyDct4W1/OPM9O3Zf2oeFtbu7kme9Jk5bNS3xcKX/V1dJynwzK9wdAtk4VPkPHVdn/3KyofjY5Azwfykmz5Ok9M6fV6E5Wr0u7vnJQ+rM3f9YZK9TEUPfuAs/JpyYxKNZFMOQuf6gudvEMlZTgcDq+0hVLzeDwBKitC2lpfoOcdDQ9Q9Wkzmxs9DKk/wd6ux/F4vK5K0OptmUimN8PtPt8wlfZR3bDRMkrOL9gu5ieppJjMZvIRmRQaOfM1Ku2j6luqM3D38sUdp9tln+I4zmiz2bxmzsxrNA16RG5euVwu0dQD6HT6JgGBMbVKVc5m0uNU3qPqPZT+HWBhM4PQDqlDcina5VcMftMxmQcgUqYEzEA1BMCERbT2Pbvhogl7VDUMD0SesACq5ckxWRO52cS8gjAuk6iEES6ToV1j4kwUhCuiWCmS8lUGALCkqb7Ofrr7M+c/fwyG+QEYORClGnE99gAAAABJRU5ErkJggg=='
        config_grande_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABsAAAAaCAYAAABGiCfwAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAG6SURBVEhL7ZZBSsNAFIaf4t6NG6HNDRR0obT2BgoKaoO5QUVEKUpvYKl6DFNbj2Ha4saFN2jqPWL+57wyJjNpApKF+MEwj5nJ/Jn3v0m7FMVQSSyrvhT+rlghz4LRmILxhGPPbZLjVDnOSyGxze1dCmczjp1qlT7e3zjOS6aY3x+QP3jhjSGCk3Vu2+RUKnR+eU2NvXrcavH4hPvOTVs9aQFiJp7852h1bf1H2z88VrNRdNd7SM1jLAurGDbGBmA6DbklwdhrMOIea1sXV2rGjLUakRaA1KEQTMWAMaRSfFyEVQw+APgldO8f6eDohAsFsaCvyUSdcA7SsrG1w2kxeSRzaLpH+rwp5SAlJg8lzRYRIB5hTMf2rJD7C8K+qXRJnPQxDD9VZEGJzsFbyyn06pKrYEujVC/mYYUJY+lDEEJ4WPKPHptjU2yoC0ladY9NWO9ZUiwLEbN5JWSU/lhF8GLGLQnG9HVyXawo0RR4S7yt3kwe6Q2+ZrGiNFPIR9XvD8k7a3Lc7X1fZHyIcSL9Q+y5p/E6l+etKNGFwBe9EhEXpdDvGTzyB0OOG/Uan6wI//+ufoUSxYi+ANWxfhXY5qMWAAAAAElFTkSuQmCC'
        config_peque_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABMAAAASCAYAAAC5DOVpAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAF6SURBVDhPrZNfSsNAEMZH8d0XX4QmN1DQB8U/N1BQUBvsDSoiSlF6A0vVY5haPYZpeo4m3iPmm84s020SX/zBkGFnd3bm28lKUUL/RGOyZJJSkk7Z70RtCsOA/VqQrI6tnb1ifWOTDf5fLFQWj8YUj78oDALK8pwr6z/1KGy16ObugY6PDks7KNen/O0/9uSkwClL3uMPV4XaydmFRIviefi6FMeaxSXDQWwAs1nG5oO172TCX+zt3t5LZM6qFMhlA7QGoavExhpahQRVuGTQAUAvZfDyRqfnl7S9u8++YvcsgLL11ao0si9qNbJxlYR00RdTkwDVyB8P/6xr04d1k3bU93XMsh/xBNyqVdjX0VGpa1NfH3FIBXg0kBCJENT+8cVhHMIBm0jbthoDN2d+siY0mb0AmNFIxYMWOZsP1uw+HSeHJOVbcJu1Ko2sQVfLmuR0P208+qTOdZv9wXA+qPjRUZH90TvRVbkv4rhDki4BXexLwm+mKH4BKpmIg++NXgYAAAAASUVORK5CYII='
        explorar_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAYAAAAiwE4nAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANrSURBVEhL3ZRfSFNRHMfvvTPntP1x98/uXF5XFnrLkTrd+jPLVRoiFRn0kkF/oYdegqinHoLoNYge6qEehP5AJERZBhVEpGkFJmnNUqdLp3eG07ZubvPe7rmdoNv+uPXnpQ+M3+HzO4cvd5zzQ/57UFiTYjabl5SUss1fI7H6t573bqawEDGRpD83TzMwx4daH7S3n4db0yJlYM3G2uO9fZ6z0hLsy5LlL6xxOvjXr7pWTExMjEGVkqSBlY61rYNDQ42CiH6lCdxLm4iWWDQ6plKpstQ5OcsiUWFnb19/OdgLvpo06k49fvTwjHw4U+yONbd0+SZOh1OfXDUbjkEdh8ViKbJVOEQ9YRZB1el0BthKn6pqxwGdkQpocWq6yGploU4KCHXVbukBoa6N7hdQp48Wp4NaIx1iV650QLUgBQUWBgSC3/r1rj1QJwSDVaaUZRtRQYywJcXP3vb3d0O9IOPjY6Ory9iLYB0VkGZZJkERqNUZ5K9ahKEtssgAbmL8MiIIc8FgkIEqIYrA6eBsA4KKKACqtPH5fO8EVOT9kwGr0WgkoI5DEchxU1YRxdTDw0NPoUqbcDgcoknKK700kaIoK9RxKAIpEh/FUFRLkskPpGIywDHSy573+/2DUMWhCNQb9D5Q6YKCBllkgN1etQNUFBFiMzMz07JMgCIwT6PukBeY6qhcMyBbrS4URSx7eXHxE6gW5uf3VF+/NaNQaTJNSpNpymaz1UGVHvsOHGwDgWBUgSkCdUoqKh1XQWB5leM6VElR/KWAl91dp8AwHvX5ECNl8W6odZ+ArYQsL1nVPTg8shlVYYQKQd5AnRRpjxKO4/xrnVUDAoLtAqGT3FRdWZmtvIhhcJ7/8pHn+VC103mYKVq6ezY0dzUc/vJ9YKNCBMNUBE2bAlOBgEd2CUj4wLMkmpqa9ubj5P4bN1trJBUV54Xg964C6c0RIxH+8yGcoE9+8I5uN5lIr2Gx5tzLF91X4B4FKSeKWsLt3nQkEhMqZ2c/53sGP7ikAyJJkF4TiT+Zj0U9Xc87L8HtSIW9+trQyMfdFtocNOhzT3d2PLsgSsD230ej0eTanetu/7h0LMtW/86YzAi9Xp+/tWFb8Efo3bZ7n2BLJu6W/ilgyjy4f8cAbjrDFCI56uwe2Pr3ZEvAJQRBvgGc/iT8lYhktgAAAABJRU5ErkJggg=='
        flechita_inversa_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABUAAAAWCAYAAAAvg9c4AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADRSURBVEhLY/wPBAxUBkxQmqpgGBv66u07KAs3IMnQqzfvMDR0T2OYOn85VAQ7INpQkIFT568Au9TByhQqigOAkhQhcOXG7f/BKYVg/PLNW6gobkDQUFINBAG8hsIMrOueSrSBIIDTUHINBAGcEfXq7Xsw/foN4SSEAaCGYwUw12aWN1PH+zAAMoxUgwmmUzFhIYZpHTVgNijhE5OjiC76QIaBDAWB7MQIBm11FTAbGyA6R4Fc3FCaBWYfOHYaTOMCJBfSIBeDLMAHRkt+agMGBgAyIBcEgb+fDwAAAABJRU5ErkJggg=='
        flechita_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABUAAAAWCAYAAAAvg9c4AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADWSURBVEhLY/wPBAxUBkxQmqpgGBn66u07KIt4gNfQqfOXMzR0TyPZYLyGOliZgmlSDSaYpECGgQwFgYbSLAYxYSEwGx8gGKYgQ0CGgUBWRQtxLga5lBjw8s3b/5nlzf+DUwr/X7lxGyqKHZCUo2BBAaKzEyMZHKFhjg5ITqeiIpAwFRMWBNNYAdi9RACQ9+u6pxLlfaIMBRkIMowYA0GAoKGkGggCeCPq6s07DPU908DJKjsxgkFbXQUqgx/gjagDx06TbCAIEJWjiMlFyGC05Kc2YGAAAI1LhoZCP97SAAAAAElFTkSuQmCC'
        hitler_encripted = 'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAjCAMAAAC0CkrjAAAAgVBMVEUJCQmBgYF3d3eXl5cPDw8LCwtwcHAFBQUCAgIMDAyKioqOjo4VFRVkZGSRkZGurq5VVVWUlJScnJyqqqpLS0uzs7NpaWleXl6GhoakpKRBQUGgoKB8fHy2trYfHx+6urozMzPW1tbr6+vi4uLAwMDNzc0mJibFxcUsLCzz8/P9/f12W4ygAAACqUlEQVQ4y01T6darKgxlEhQBGRzAua229rz/A97gd4ab1R9dbrKT7J2gCgmBIMpSqGvcV4WqsiqLEv0LARhS79Hqod3XFcF7Ud1x54oSsXUciPTeYduugomC3QEwBKTu2nWfB0Rww8WE+gMDsSgA7sPj9fx+fz1fC1mr/8NIMPW2/ny9fh58WvWXvMzFC3VZk7mf+cEzvtGf1m6YrXs7h207X8/X4/VddlbcAQPn33qNNnZbF7YlpGNbBpYHLipUQvFK7Xbo62ZpvDdGNlO0tx6QLaqyZJfmnLjUQWpI6QjYsh/81qQc65mQWE/L8TmPx3mG9i85cJd77eRMZpm6zwnVH8dYAXEBnUMuiGYpJZxE6sPitXV+VFUFKEOQWxZi1UT3RAIc5vGy/GKQnmFxy8beY6tJdFMXettaoorqN3n5z01Su+ANjlIr6BlEK34cE+9R97odZmz8NCXfKvHDnrdECDZGjLm1gyYmLdu0qxLkRtVvv1fdhVTzoW2HHtc1V9X9ucjTC6H23n8+2yT5YK1txwu0vCXNK1iyvdV8Arc/DUyvLyUKgIvcGRLQ9NBzztP5fL7OZqqvKlt8a14hADkITvhMH7AIj2a6GAOfcldgCVghJZlxnGU4v98zOatYmSsXmWKi3gA8x9pE/3ge0mA4BnYvNzS+pMlE4MbSRNmA1XXCvIdryJcgUOOpMZjoGUtnHKXYhTQlivtxLUSBAnUGdAa/MI7wEBsaQupCR/UbxvMyYkdrbmGfsHMxSjI1Ke+kaZlAkvAeMqTWOtd3VPZug5UNzdS/BYI+Bi49lfCH49r7mpvlaLquSRE2bgYj+rlOEwUeoPcU18vRbUsXpqGC7KEdOKaeOolhekpjhhe4hdArFIlurSbwGY5bSglt1N2xLJ9j67j6D+qFO4G5hsGIAAAAAElFTkSuQmCC'
        home_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAYAAAAiwE4nAAAACXBIWXMAAA7DAAAOwwHHb6hkAAADKUlEQVR4Xt2W3UsUYRTGd00t7UOiggrdJUqIICGjJNekuumiD4Mka73tJokoTFG66S6/iogg/ANa3fQiyyCKLjIVLOqikkT8aGezSEIWLKUvp9+xeWWaeVd3666Fh5k57znPc86Z876zHk+SP9M0U0FGJGIUcl2UZHjy7k+6e/YeKDlqChDNRdSbPEuCEadOn92ctXrdBzABJsE4tsYEw5Nz27ptZxkCfSBCdS0CS3yMta6boda1yTHO4w1xPzAg7qWlq5QrInnYulkbA+9I4to/iUJyHwyB97SuPh4Za0GEO/AbBAN/JUrgKxAl6zBVbUqEBNFmYt6IKHGHFowh00ycu8BTaeGlhqaKBYM0Dgi3iaiIx423WhLBaQSMIlbqdLZvAbbEvNvB4hnmOgx3i+JKsZGm+3JyRsE4tkxfdvZ3u6Bs+FBL+CLBJiRm3vYC2RYfGZz1caqYgWsQ9Pt8Oc/iVkrv2yGKQVSunBBL4fmxCDkQE1G6scNJKAMEl2vQ7BWqmHRussBiO0nFmXPF8lwUKPS8fN63pfN2+/7g8bK7mLx1DZc7NRX8wBZz2lM1jq4kDCO6UfkhtJT7ado0QLuGunt6A0Y0ukzD8xPblNOuq/Cr5WQqZwg3zN0b0T1er9cUYEuz1nSJa1+bTlCGRTL7piJ2FwUeUM3sYyh86x4Tuk++GHWNV9QmX6lhlyRc/DpBEfosbbOTBE8ca5Jn3peHCX2Ul18wFWoNz7rUVFfqTiHZNq7KdYLSKsFchUJaW32+SoZEVUorldhkTVXlBU2FMnwrnPZ4QyPZzTidb1y/eph2+hHLZ5BKmNhmhueF05ctVMxUy5S7viA6wQwcFVyJ+/2+CMYI77BDFhkeV2KY5YWngbkviyLStXQJi8utAE2nfptESInJkWeDcGaCNSDf+Y/AVSHv6K0QhsJtJ2nNBLcj4JOVhM9qkxBK9rJdsjnyvlg+Ma7TxDYIR1Fg1x1nxq4DmE9R7sEjpa9xlFZNAjVEcpXsJUaG4Y+TSNcKTiQ/r8Cwr2lPfPn+scfqGQy/5axEVazEKdj5Zg8LhukhA1arS+L/t/0CxAJAk5AIk/kAAAAASUVORK5CYII='
        kkk_encripted = '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'
        listas_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAYAAAAiwE4nAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANVSURBVEhL5ZbLaxNBHMdnZptH82iT3c2j2tomBGp9Va3WB0q9e5C20KPgQcSjBw/i41/w5kkQCmo9CR4VLAh6slWroCgIpZWaVNM86iZmX/5+4yTGbuJjPfpJJt/d787Od2YzmQwlv4ABFLAB1I2IagSvWwAeoyL8QgtaBiqKEtu+c9epleynk5DGmNQRYpKkSpLUKaq0Ra/VllQ5cvfJ40fnWgW3DOyKJlZAYFjwJsQLHx0wXl6XEssgNrywAiUS+FA4NrXsGtyjw9h9xKJmaS2bENfaM7Jv9CIEfhzaMXxVWH9Nb1//ybCSLCSSPYeE1YAJbQBf1jDq61cvznHDBctLi9PUtnRZjU8Jq4EjkFAGj49Q+L5Q/wmJMZ84bOAIhEpeEJpKpUa+Oy6h0HVKPeKsgSPQ4/FEqMRi0ai8WViugMntI9KfBPp8cVS/3x/iBhCPx9MwCYrdao/ZothhOVmGjvpF9TpUItLvA30+fxI1EAh0cwPQNC0fV5U3qiI/xRJT5LmYLM/H5OgzOJ+Px5S3g4Nbj4jqJJPJHIAlI8g62MZOODl+YtLGXk9MTF4R1l9z8OChKWxj9PDRB8Jq4JylAllR+sQhESsZB5c7BGbxT6AnqsNT8gVRQ+HQEDeaaBs4MDCwBwOwsfHxictdStLCEpYTJpZQNG40lzNnz07XQxVV3YLa6Q84Jl7bwFQqPcKHBKTTmVFhtyX/Ob+EizgeG4ZR42YL2gYiuPjCzcb09I3T/Zti+7H0qN27YpHgtkjQmwl4SF/QS7eg3pm5faEeWNG0Im/gT6hPmpu3ZvjNbhgbO3YK28C2hNXglyN0S6VaKaOWCoXn3GjCEQhPsIL6cmHhPjdcUCwWs6hftPV33GjCEQi9W0SdnX14nRsu+Fqtrlu2uQZTwDF5HIFfK5Ul1FK5tMoNF+RyuffUolXTNDVhNXAEwv/YHKppsWvccEFmcIj/eZcKa/e40UTrLYac0CBZg22CAfsGg1ikYtlWCXYWa8S2yrAsd2E9asMWg9EoIzRgM+KFxsR2AzdYtl3Or/Z+P/9By0Bk996R8+VyZdyybR1+Xjo0YIDWYH9WtUxzHR5X3jD0VV2vfTB0I8ckFvJ6/WlYmCLZleVLopn/DkK+AWbaOqQAQouLAAAAAElFTkSuQmCC'
        more_options_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAO+SURBVEhL3ZZLbBNHGMd3ZteO7X141/GubfyKYyhOiRHGNIgEUQwFiV4rkKh6KJVQL0hVxQGJI+JY9dATFxAnxAVRVYgD4oAqHlKgDZQkLW1QSngojjeuHzhx7Ky332wG6BJDgrn1Z61mvm/m2/88vtkx878D0XJFEEKCy+XKQLVqGMY48ZnAi3IRIPU3saIQCDgdDkcfiOQ8Hs9+X7fqeTKdjwUDgVmQaYQC6s+N+vy18fGxK5VKpUTDlvFWISrSL8vyCRDa3Wq1Zqv1JmcaDGawiRmT/JA1K031P5Jl/tSd4eHTVvBrvEmIxRh7OI6LK4ryPYhlQOSfWq12hheEa9BY1HX9SSqVyrk8ws6FRrNnYmJyBwlUNf/fDx+MbbXeshIg0u31eo8TkUgkMq2q6k+wbAdpc1u2fDTwlaQE8uRZu37DMHW3hy7VelEUj0Sj0TKIPNM07RLMLEGal3q9neS6D2+C2PTGzdmz1LUcmAloiIeDweDtcDjyDGZ1FER6SNNSj9UhKNqk4FOnREkKUddyJEW979eCozzPH4AZitT9zoiy+me8d+1FatqJRKP9ok97Guvp/Zq6OkbVAntFxf8HNe1LEosnDiETITiBj6mrYwoz+SuwrcaaNWErG21C+cLs9hZqGVOPJi9T13tiYqdbOE5qNqGZwkwYDmCTmhZuSbkQCse+o6aFIKu/iYo6Rk0LQfbf4r3dI9S0MEEHEsxF6jYhOOIGrb6EY7lUda7+GTWXwEgyEWNLFMQgP2JZhZpLYNOp68UUtV6xIb3pB0jL994fQigU+oCcp+zANivzbDNqGc2rMDKc2Zz9gro6Jt7TewgKLHulKiwftglVyqUxyDq2+rz+DXV1jD5b+gSxWO1ycHfhPCL7HpkMSQQ8U9DjuV27rWzphG2DQ0cKxeIWUh8dvf8j3F/2vSfKg0NDn3v9ocW+dLbUn04P0qZ3QvIF5uAdJgz2MHUth4jt2vPpFOmYzgyY8NXmadOq2JjJnoHY5tCO3C3qsmj7RU4mkym9PPc7qceiUcaBW1+O/PrLeRgDD7d2HUoOmlioz5MS6Ib7qsxLvmETIzf4zOfFQpzEv6CtEJlVIpFY15fOPLh+46blEz1dFyul4nVY7gK8WIEu7mazOUHE3W73noXGYsFgUHKhVjkIfeasoP+w4h3z8c7csZF749+yLJrv4pg8JCo5lC14SOwi/V/yV7lcPtloNO6RmHas6jIjOJ3OLIx8X71ev8pgNuER5XO1kr6JNjtA7CG57qn9GgzzL7AwNw7InubpAAAAAElFTkSuQmCC'
        msg_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANXSURBVEhL7ZZLTBNBGMdnZtttYWlpaSmPosESohgrIA8FAY0HNUZNBOPRu8SDiQSVg2cTLx70gAcTYzx4MEYvxsSD8ZWYKIkJPlaKPLQIpbSQ7WOX7sNvl7HpBppohRu/tDv/+fbr/nd2Z74p2mS9wbTNsqel5VC1f+vgfDRKJEmMyLIsIE1TESYWgjGD4UtTDQgmLGGIDRNswYhYoSUMwxQ7SrjIGP9laGJiYoymGqwydJRVJCGsYayKGiIsmJkM4AdYQwg+Rk+XmICvcYogrKo4QwjmVs4jVOlxBnmeH6VdM7sbG884Pb6FlvZ9D7ds2Rqk4X+CZdmipqbmY8Hmdq3UW6WdO3+B3twaBOobXoBhNBAItNJQwbS2tZ3SDXVjeA3ZJ6k/iiyqqiSRiuWZmZmvNFQwyWQyTqUJk6GmIUVvRFFMrEQKJ51KLVGJ8o6QEGTDDPE53RW/cpMKIbaUfkZlfkOEGDscCJhWOt2+tMPlC63E/55ip/uJPg9o14AAVJoN4T5YVVMW6wK1j7zl3o+IaHYY7SxX6hnBhFhp2prYOecw5H0ghKn2uN0jwV077tNT+Q1hzcLiZlycnX08zn/aK8Tma8q9rhuwropKXL5YSVn5VF399ks0HVVW+/v0m9FfAWNhaottlqHEYrR1IsQfzkjia5pmwmSo6UsXqPH7dxoBYHyMvybEow1Oju2HBCWysHjVUVYplHorpJSUua2PPCMJTcml+JH5yFz2vdntdgeVSAGoNBtarJYKvT1+4uSgEcgh/GP6XiIeCbgdRac97tI3iqLN+Mpc/Yn4fBBm5BxNy1LMcS4qTZgMWavNT2Vepqcmn06O80fBfFto7NsDGl4FlF+VStCw4Cgmw/VEEATTTP3DhhmKaVGg0sSGGeaWtryPVIViSuV/A0svu63lGprKV8f+7uuf+dBA1/5O1NO5d/Tlq5d3Ywuxn9KylJIzspQ7EfR6pV9JhQ+GDmzUy6KYFmZn50KZzLLY3tH1/PPXbz2XBy+iK4MDWZ9V9VLfUqhcF+4M33rT19fbRburDXW6Dxy8abNxvYjB1lQi+V2WMzFFkVMwQBkGpUABWLkp+GNgbHb6AUoUXMy4HlQdR1VVtf39u7dnw+HwlJG7ySaFgdBvyvM+VA79KIsAAAAASUVORK5CYII='
        notifications_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAYAAAAiwE4nAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAMFSURBVEhL3ZVLTBNBGMd3W9pt6dItbaF1aZu0UKi22Ehti1BeiSAJCWKQxMhVrybGxHjmRExMPBhvHjUGUSHRxJORIMbEEOIrEHlsKURAoQ2vslv6cGc6HJaWlq0X4y+Z/L/5z7f5ZnZ2ZrH/HhxpTmi6wmKz2ZrlCoWVZWOdGI6nCLl8Nr7PvWMW5seWl5eDKDUveQt6/f7rP+ZDD/mwKO0IoWljREuRAxPj4/eRlZOcBT3e+uE5ZrGXD/f1Ou2UWqV4kEwm46srK59ok/ny1k60b30jXAdydaWasYXZ6VYQF4THd+4lpT+RKtEZt5wu1yVkZ0VdalgDuVZbVc68Iwk0Nd+ExbTGHWTl5aAo6h6JBKmAX+vha7wkDLqSnrSTn63ImgGoxWYfgcZx8fvr+8BMwYyRdWxIbVmIfzaOulnJWKGMUDQBPemoegQNESTZaAsvUjVFVaSdTDIKclzMCnQzEn4DDRFEo7sMUP7Y3oBGFjIKbm/v1gKVFkll0CgAluVOoTA/YP9AIwhCgSxRoP1fRd0MBCukadqMQv7VciwKRZFKJvdSOE6ibgaCgjU1jgsoLBhjeVlQIsHlbrcbfnyHERSUSKXwvvT5zkagUQCUhlrgRUZRmsq0I0RQUEWSTqBKgviC80BTJOoSyg209Xx71stc8AdIJLFqoEww1NLd0/uWi3Gbif0EG0/E9/j6EmWxspxj2TCWSsErDPgxLrYpkxNqklRV8MVs36ZnTGBscnKKAnoYwSoaAi0T32d+NKDuXxFobMBejz7PeEsCw2Q2u5yu2n7wC+IHcBmh9L7/8LEDjHnrTg9YbZWtFovFt/F7fY6i1CZFcbFm8O49+Oyd27egHmAxmbD+q1fEbYterzfUnvHBc9nR2TWEbIiTp+tiLxwDbZAHDeUk7wzqPJ7u+cWfoyC2mM1YW1vga5m+3DH07IUstLQEc16NDGNNgUZxq8mF3V7dfrCSw+3xk6cpGQ9KzYuoWdlrHP1KpaqNP64kpVZ9XgwywwzDzKLhfxEM+wPxPeq9+XXcCgAAAABJRU5ErkJggg=='
        profile_big_encripted = 'iVBORw0KGgoAAAANSUhEUgAAACMAAAAoCAMAAABDwLOoAAAAIGNIUk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAADnUExURa+4vq63vbG5v7nBxsHIzsTL0LrBx9LY3OTo6+zv8u7x9MDHzOLl6fP1+PX3+rvDyOTn6/T2+bK7wdjc4cHIzezv8/X2+bC5v9LX3LO8wt3i5ra+xOPn6+To7LW9w+Hl6bG6wNfd4cnP1PHz9rjAxePn6sfO0rK7wM/V2rO7wcrQ1eXo7LrCx9bb39ne4sPKz87U2Nbc4Nje4r/HzNTa3ubq7e/y9fL0+Oru8fX3+b/Gy+Dk6PL1+LzDydzg5LC5vszT1/Dz9s/V2ePm6sPJz6+5vtDW2tvf47a+w7jAxufq7uns7/////XZPbMAAAABYktHREz3bxDzAAAAB3RJTUUH5wkIFRI0TJwu+QAAAVFJREFUOMvN02mfgVAUBvCSUeJeriVLhigiGQwh+75+/+8zk0Hh3F7P8/r/6zydUwzzv8M68RcBLvgR5AJ+KsQLYTEs8CE6iUQRdoKiERqJxck98RhMEkniJpkA+6bS0oNI6RTUO5NFnuegbAYwuTz2GJzPAaPkwpMpyCxgPp+MAJli6cmUikBppUy8KSvQy1dUD1Er4A61qjsMVzV40TXxjrBYo9xLr98QFus67agNo6kSTNSm0WDoMY3WV8swfYSitTvd726nrSkwYPVe3xoMEULDgdXv6dDdOX5E7Nt72WTEc+9kPJk+3WI6Gb+SSJO8pvnyUc8E8h5h5iXynECZyy5ZLFegWS0X7uYsDBpsudtcIwIHrR9tNphi8ObWiN2KEsVI4vZv3bs9bdTvsP3uahIHm2rsw/WfZo/UOk6hozOMPZ19zPl0NebFx1xMlvkBCSY6i4zNmg8AAAAldEVYdGRhdGU6Y3JlYXRlADIwMjMtMDktMDhUMjE6MTc6NTUrMDA6MDCdxjFyAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIzLTA5LTA4VDIxOjE3OjU1KzAwOjAw7JuJzgAAACh0RVh0ZGF0ZTp0aW1lc3RhbXAAMjAyMy0wOS0wOFQyMToxODo1MiswMDowMI8izRIAAAAASUVORK5CYII='
        profile_uno_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAJySURBVEhLvZVLaxNRFMfPuZNHm5igFhVDKVpcxtiWCJWupCvBlTQihZgwwWJwpd8gX0DcSCEu+kCC4AcQd+1CEITUZlEQCq1S8IFiIT4y6cw9nkkPRZlMEkrqD8I9/3Mn58/ce+4d+B+gjF0hIszn82eCWsdxYKCeSCQ+l0olLdMd6WriFjfN29MK1HUiGJI0IOJ3DfrFyMj5l93MOppkMhkjfixyj4tflpQXBbVAIPyoXC7vScaDkrEt8Wj0RkcDFw0p27JuiWqLr4lpmjECuiayMwqmC4XCSVEefE3QcVI8BPdVFwgMsu1xUR78TZQ6K2GvnJLRg68Jd5UlYU9wtzUl9OC/8Y6zKVFPkONsSejB12R4dPQdb/xHkV2gr/VGoybCgyGjh9XVVUqnU++B1BRL/zfmJtagHlcqlU+iPfiauFSrtW9j48ltXvEUAoYk/Rf0CxTNLywsv5VEWzqa3J+ZGZyvPNtJJi+uGAH1A4itEPYQaIffbcVqOk+Wl59uuc+93tiw5W8e2l4ruVzuOLtnuNAUadjmh96AYWyGw40v9bpqxmI6ZFkDp7k7Lrg3As+f45P/ygF4vrS0tCtlDvCY8E07oZDm+IBFJdU7CD81YXlxcbEqmRb/LBfftlcVYJEN2qx/T4QU4uT4RGp3bW2d93KfAxPTzKaRjLvu1S6pw4IEaiydvvShWl1vHYFWaxaLsydA450+GLRArqNtmpud5bpMy6T5O3STpyJu3D8wMhhy63KUzWaHgoZ6yHGnA3c4EBxUgQcqGFSTLPtv4OJ+Asi+okBTUlJHA9fnjsVhkUcD13eXKcbfAjqqHwDE/gAggd2dx830LAAAAABJRU5ErkJggg=='
        saves_encripted = 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAZCAYAAAArK+5dAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANjSURBVEhLtZbbSxRRHMfnvjPO7uzOqqOrKaYiLhVhaIaJRUoUURIZSCL1GvjQQ75HRQ9B9Af0IIEE0YV6qJeCELyDFEZG99JSdMvLmuuuuzPT+Z09O+44GrtBH1h+5/c9M/s9l985u9T/hiYRw7JsqaYVtMYTCe1naO4Sx3HFhmEsk+6NmKRPT6abYzPw5gVM3YjP0zodp2hjzuuW1EQi8QV9kYm6w8mnksCXRyLRFZNm6zhOKFQ88scf3782km4Ly8Dvzz2tM0yvx+19E14IXVsOh1/IsnyOYRgBdTtGaZpmOBaLffAoSqmaq10N/VooClaV3xkeHOggj9jZXl5xU/bnzxcGAl1EypiKysrLMPvzXRdgprZVYUiEERmMYSbWYmtLRMoYtIxR0nRgM4Co6/qWD28FemcN4moksoqFNCwDNC88NbLmWZEyiEZXHBW3bsCwnMlQrCAICpEyBhnEIK6uxLY2YFiaYxnezwu8TKSM0ckeoKr9jYU0LAOO4yWILMu5sJAFqHSgeqh4LB7BQhqWgSjl+CAKAp+DhSxA+8ZDTJiG47xYBorbUwDRJbjcWMiClAFt4hNvwzLw5aoBiKIoZb3JyICDqJsmzMBmYhkU5mvbIMqKR8VCFqBLUYRooFsSC2msb7Ig4vr3KoofCxtAowygTyFJbfC8gCuPZmnbNQFYBim8infjDGifz3fU4y+Y3rG7dqY6GLwOWrIriegS8bJyLOc4pCkD64Wi4uIS0gTYtvb2UZOTnkIyOTVFzYQWu+vq63tQag1OlFzYwCWKjjPkmIFPVb0QJUnac6z1VOLZ875ayBv3N1AnTxzHd837T5Nnd9Xs1Xmer4JcknJw5THoEKFgm53DAAgGg92C7BvrHxjEefPBxpEnjx8wt3tuFVdXlvWCBrOp3lnz7sCh5kcMm6wigePxZqfjMOgfGKKmQ4uwzlRpSQklskb7w/v39qEUXbjmwsjwUOfKYqgC+sDk1fhE69JytA2edyseR4FsYpAcNSzJ65ej3Ozs7F0spIHu/88T42NlRZp6A3IwAlQ1Nw830kgZ2A5HU0NdH1oSFjW3/EFHN+i3txMTF/N88hUi/Z2Ww0fG0MaZiqK0EClj0L+REni3/UzHLEodZwGjaVonaf4zstvdRJoEivoDTzMUlOdM4HAAAAAASUVORK5CYII='
        stalin_encripted = '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'
        
        #desencriptar
        verification_decoded = base64.b64decode(verification_encripted)
        captura_perfil_decoded = base64.b64decode(captura_perfil_encripted)
        config_grande_decoded = base64.b64decode(config_grande_encripted)
        config_peque_decoded = base64.b64decode(config_peque_encripted)
        explorar_decoded = base64.b64decode(explorar_encripted)
        flechita_decoded = base64.b64decode(flechita_encripted)
        flechita_inversa_decoded = base64.b64decode(flechita_inversa_encripted)
        hitler_decoded = base64.b64decode(hitler_encripted)
        home_decoded = base64.b64decode(home_encripted)
        kkk_decoded = base64.b64decode(kkk_encripted)
        listas_decoded = base64.b64decode(listas_encripted)
        more_options_decoded = base64.b64decode(more_options_encripted)
        msg_decoded = base64.b64decode(msg_encripted)
        notifications_decoded = base64.b64decode(notifications_encripted)
        profile_big_decoded = base64.b64decode(profile_big_encripted)
        profile_uno_decoded = base64.b64decode(profile_uno_encripted)
        saves_decoded = base64.b64decode(saves_encripted)
        stalin_decoded = base64.b64decode(stalin_encripted)
        #convert to bytes string
        verification_bytes = io.BytesIO(verification_decoded)
        captura_perfil_bytes = io.BytesIO(captura_perfil_decoded)
        config_grande_bytes = io.BytesIO(config_grande_decoded)
        config_peque_bytes = io.BytesIO(config_peque_decoded)
        explorar_bytes = io.BytesIO(explorar_decoded)
        flechita_bytes = io.BytesIO(flechita_decoded)
        flechita_inversa_bytes = io.BytesIO(flechita_inversa_decoded)
        hitler_bytes = io.BytesIO(hitler_decoded)
        home_bytes = io.BytesIO(home_decoded)
        kkk_bytes = io.BytesIO(kkk_decoded)
        listas_bytes = io.BytesIO(listas_decoded)
        more_options_bytes = io.BytesIO(more_options_decoded)
        msg_bytes = io.BytesIO(msg_decoded)
        notifications_bytes = io.BytesIO(notifications_decoded)
        profile_big_bytes = io.BytesIO(profile_big_decoded)
        profile_uno_bytes = io.BytesIO(profile_uno_decoded)
        saves_bytes = io.BytesIO(saves_decoded)
        stalin_bytes = io.BytesIO(stalin_decoded)
        #convert bytes to pillow img
        verification_pil = Image.open(verification_bytes)
        captura_perfil_pil = Image.open(captura_perfil_bytes)
        config_grande_pil = Image.open(config_grande_bytes)
        config_peque_pil = Image.open(config_peque_bytes)
        explorar_pil = Image.open(explorar_bytes)
        flechita_pil = Image.open(flechita_bytes)
        flechita_inversa_pil = Image.open(flechita_inversa_bytes)
        hitler_pil = Image.open(hitler_bytes)
        home_pil = Image.open(home_bytes)
        kkk_pil = Image.open(kkk_bytes)
        listas_pil = Image.open(listas_bytes)
        more_options_pil = Image.open(more_options_bytes)
        msg_pil = Image.open(msg_bytes)
        notifications_pil = Image.open(notifications_bytes)
        profile_big_pil = Image.open(profile_big_bytes)
        profile_uno_pil = Image.open(profile_uno_bytes)
        saves_pil = Image.open(saves_bytes)
        stalin_pil = Image.open(stalin_bytes)
        #convert pil img to tkinter img
        


        verification_tk = ImageTk.PhotoImage(verification_pil)
        captura_perfil_tk = ImageTk.PhotoImage(captura_perfil_pil)
        config_grande_tk = ImageTk.PhotoImage(config_grande_pil)
        config_peque_tk = ImageTk.PhotoImage(config_peque_pil)
        explorar_tk = ImageTk.PhotoImage(explorar_pil)
        flechita_tk = ImageTk.PhotoImage(flechita_pil)
        flechita_inversa_tk = ImageTk.PhotoImage(flechita_inversa_pil)
        hitler_tk = ImageTk.PhotoImage(hitler_pil)
        home_tk = ImageTk.PhotoImage(home_pil)
        kkk_tk = ImageTk.PhotoImage(kkk_pil)
        listas_tk = ImageTk.PhotoImage(listas_pil)
        more_options_tk = ImageTk.PhotoImage(more_options_pil)
        msg_tk = ImageTk.PhotoImage(msg_pil)
        notifications_tk = ImageTk.PhotoImage(notifications_pil)
        profile_big_tk = ImageTk.PhotoImage(profile_big_pil)
        profile_uno_tk = ImageTk.PhotoImage(profile_uno_pil)
        saves_tk = ImageTk.PhotoImage(saves_pil)
        stalin_tk = ImageTk.PhotoImage(stalin_pil)
        #global variables
        self.home_img = home_tk
        self.explore_img = explorar_tk
        self.notifications_img = notifications_tk
        self.msg_img = msg_tk
        self.listas_img = listas_tk
        self.saves_img = saves_tk
        self.verification_img = verification_tk
        self.profile1_img = profile_uno_tk
        self.more_options_img = more_options_tk
        self.profile2_img = profile_big_tk
        self.hitler_img = hitler_tk
        self.KKK_img = kkk_tk

        self.post1_img = profile_uno_tk
        self.config_busqueda_explorar_img = config_peque_tk
        self.flechita_img = flechita_tk
        self.flechita_inversa_img = flechita_inversa_tk
        self.stalin_img = stalin_tk


        #self.save_img = PhotoImage(file=ruta_imagenes23)
        # MARK: BOTONES
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Boton invisible
        self.boton_invisible = ttk.Button(self.menu_frame)
        self.boton_invisible.grid(padx=60, row=0, column=0)
        self.boton_invisible.config(state='disabled')

        # MARK: BOTONES MENU FRAME

        self.home = ttk.Button(self.menu_frame, image=self.home_img, compound='left', text='Inicio', style="Custom.TButton", command=self.home_boton)
        self.home.grid(row=0, column=0, pady=5, sticky="ew")

        self.explore = ttk.Button(self.menu_frame, image=self.explore_img, compound='left', text='Explorar', style="Custom.TButton", command=self.explorar)
        self.explore.grid(row=1, pady=5, column=0, sticky="ew")

        self.notifications = ttk.Button(self.menu_frame, image=self.notifications_img, compound='left', text='Notificaciones', style="Custom.TButton", command=self.notificaciones)
        self.notifications.grid(row=2, pady=5, column=0, sticky="ew")

        self.msg = ttk.Button(self.menu_frame, image=self.msg_img, compound='left', text='Mensajes', style="Custom.TButton", command=self.pulsar_boton_msg)
        self.msg.grid(row=3, pady=5, column=0, sticky="ew")

        self.listas = ttk.Button(self.menu_frame, image=self.listas_img, compound='left', text='Listas', style="Custom.TButton", command=self.press_list_button,)
        self.listas.grid(row=4, pady=5, column=0, sticky="ew")

        self.saves = ttk.Button(self.menu_frame, image=self.saves_img, compound='left', text='Guardados', style="Custom.TButton",command=self.ventana_emergente_prueba)
        self.saves.grid(row=5, column=0, pady=5, sticky="ew")

        self.verification = ttk.Button(self.menu_frame, image=self.verification_img, compound='left', text='Verificado', style='Custom.TButton',command=self.ventana_emergente_prueba)
        self.verification.grid(row=6, column=0, pady=5, sticky='ew')

        self.profile1 = ttk.Button(self.menu_frame, image=self.profile1_img, compound='left', text='Perfil', style='Custom.TButton',command=self.ventana_emergente_prueba)
        self.profile1.grid(row=7, column=0, pady=5, sticky='ew')

        self.more_options = ttk.Button(self.menu_frame, image=self.more_options_img, compound='left', text='Más opciones', style='Custom.TButton', command=self.press_mas_opciones)
        self.more_options.grid(row=8, column=0,pady=5, sticky='ew')
        if self.logeado == True:
            self.profile2 = ttk.Button(self.menu_frame, image=self.profile2_img, compound='left', text=self.nombre_usuario_publico, style="Custom.TButton",command=self.usuario)
        else:
            self.profile2 = ttk.Button(self.menu_frame, image=self.profile2_img, compound='left', text='Usuario', style="Custom.TButton",command=self.usuario)
        self.profile2.grid(row=9, column=0,pady=390, sticky="ew")

        #MARK: BOTONES POSTS FRAME
        self.estilo_para_ti1 = Font(family='Berlin Sans FB', size=14, weight='bold')
        self.estilo_siguiendo1 = Font(family='Berlin Sans FB', size=14)
        self.para_ti_button = tk.Button(self.frame_para_ti_o_siguiendo, text='Para ti', command=self.para_ti, font=self.estilo_para_ti1)
        self.para_ti_button.grid(row=0, column=0, padx=315, sticky='ew')
        self.siguiendo_button = tk.Button(self.frame_para_ti_o_siguiendo, text='Siguiendo', command=self.siguiendo, font=self.estilo_siguiendo1)
        self.siguiendo_button.grid(row=0, column=1, padx=315, sticky='ew')

        

        # self.pad_invisible2 = ttk.Label(self.frame_para_ti)
        # self.pad_invisible2.grid(padx=710, pady=700)
        # self.pad_invisible2.configure(state='disabled')
        #publicar post
        self.foto_escribir_post = ttk.Label(frame_escribir_post, image=self.profile2_img)
        self.foto_escribir_post.grid(row=0, column=0, padx=10, pady=0)
        self.entry_escribir_post = ttk.Entry(frame_escribir_post)
        self.entry_escribir_post.grid(row=0, column=1, padx=0, pady=20, sticky='ew')
        self.pad_escribir_post_invisible = tk.Label(self.entry_escribir_post)
        self.pad_escribir_post_invisible.grid(padx=680, pady=0)
        self.pad_escribir_post_invisible.configure(state='disabled')
        self.boton_publicar_post = ttk.Button(frame_escribir_post, image=self.flechita_img, style='Custom.TButton', command=self.publicar_post)
        self.boton_publicar_post.grid(row=0, column=2, padx=0, pady=0)

        #airstrike_company
        self.post_foto_airstrike_company = ttk.Label(frame_post_airstrike_company)
        self.post_foto_airstrike_company.grid(row=0, rowspan=2, column=0, pady=3, padx=5)
        self.post_nombre_airstrike_company = ttk.Label(frame_post_airstrike_company, text='airstrike_company', style='Nombree.TLabel')
        self.post_nombre_airstrike_company.grid(row=0, column=1, padx=0, pady=0)
        self.post_nombre2_airstrike_company = ttk.Label(frame_post_airstrike_company, text='@airstrike_company_oficial', style='Usuario.TLabel')
        self.post_nombre2_airstrike_company.grid(row=0, column=2, padx=0, pady=0)
        self.post_airstrike_company = ttk.Label(frame_post_airstrike_company, text='----')
        self.post_airstrike_company.grid(row=1, column=1)
        self.post_airstrike_company2 = ttk.Label(frame_post_airstrike_company, text='¡Prueba nuestro nuevo software para lanzar misiles balisticos desde nuestros increibles satelites nucleares!\n Tan solo pulsa el botón para abrirlo y bombardea a quien quieras (solo para personas autorizadas).')
        self.post_airstrike_company2.grid(row=1, column=3)
        self.post_airstrike_company3 = ttk.Label(frame_post_airstrike_company, text='----------->')
        self.post_airstrike_company3.grid(row=1, column=2)
        self.balistick_rocket_button = ttk.Button(frame_post_airstrike_company, text='airstrike_company ballistic rocket launching softwar', command=airstrike_company_balistik)
        self.balistick_rocket_button.grid(row=1, column=4, padx=0)

        self.post1_foto = ttk.Label(frame_post1, image=self.post1_img)
        self.post1_foto.grid(row=0, rowspan=2, column=0, pady=3, padx=5)
        self.post1_nombre = ttk.Label(frame_post1, text='Usuario', style='Nombree.TLabel')
        self.post1_nombre.grid(row=0, column=1, padx=0, pady=0)
        self.post1_usuario = ttk.Label(frame_post1, text='@usuario', style='Usuario.TLabel')
        self.post1_usuario.grid(row=0, column=2, padx=0, pady=0)
        self.post1 = ttk.Label(frame_post1, text='-------')
        self.post1.grid(row=1, column=1)
        self.post1_2 = ttk.Label(frame_post1, text='------->')
        self.post1_2.grid(row=1, column=2)
        self.post1_real = ttk.Label(frame_post1, text='Esto es un post de ejemplo') 
        self.post1_real.grid(row=1, column=3)

        
        #MARK: BOTONES frame_r
        self.buscar = ttk.Entry(self.frame_buscar_frame_r, textvariable=self.entry_var, style='placeholder.TEntry')
        self.buscar.insert(0, self.place_holder_text)
        self.buscar.bind("<FocusIn>", self.entry_focus_in)
        self.buscar.bind("<FocusOut>", self.on_entry_focus_out)
        self.buscar.grid(row=0, column=0, pady=5, padx=0, sticky="ew")
        self.enter_buscar_frame_r = ttk.Button(self.frame_buscar_frame_r, image=self.flechita_img, command=self.pulsar_boton_buscar_frame_r)
        self.enter_buscar_frame_r.grid(row=0, column=1)

        self.verification_label = ttk.Label(frame_verification, text='Obtener verificación ✅', style='Verification.TLabel')
        self.verification_label.grid(row=3, column=0, padx=30, sticky="ew")

        self.verification_label2 = ttk.Label(frame_verification, text='Suscríbete para desbloquear nuevas funciones')
        self.verification_label2.grid(row=4, column=0,sticky='ew')

        self.w_happening_label = ttk.Label(frame_w_happening, text=' tendencias', style='Verification.TLabel')
        self.w_happening_label.grid(row=7,column=0, padx=30, sticky='ew')

        self.w_happening_but1 = ttk.Button(frame_w_happening, style="padding.TButton",command=self.ventana_emergente_prueba)
        self.w_happening_but1.grid(row=8, column=0, pady=10, sticky='ew')

        self.w_happening_but2 = ttk.Button(frame_w_happening, style="padding.TButton",command=self.ventana_emergente_prueba)
        self.w_happening_but2.grid(row=9, column=0, pady=10, sticky='ew')

        self.w_happening_but3 = ttk.Button(frame_w_happening, style="padding.TButton",command=self.ventana_emergente_prueba)
        self.w_happening_but3.grid(row=10, column=0, pady=10, sticky='ew')

        self.w_happening_but4 = ttk.Button(frame_w_happening, style="padding.TButton",command=self.ventana_emergente_prueba)
        self.w_happening_but4.grid(row=11, column=0,pady=10, sticky='ew')

        self.w_happening_but5 = ttk.Button(frame_w_happening, style="padding.TButton",command=self.ventana_emergente_prueba)
        self.w_happening_but5.grid(row=12, column=0, pady=10, sticky='ew')

        label_categoria = ttk.Label(self.w_happening_but1, text="Educación", style="Categoria.TLabel")
        label_categoria.grid(row=0, column=0, sticky="ew")
        label_nombre = ttk.Label(self.w_happening_but1, text="Porno furro", style="Nombre.TLabel")
        label_nombre.grid(row=1, column=0, sticky="ew")
        label_cantidad = ttk.Label(self.w_happening_but1, text="500 mil posts", style="Cantidad.TLabel")
        label_cantidad.grid(row=2, column=0, sticky="ew")

        label_categoria2 = ttk.Label(self.w_happening_but2, text='Informática', style="Categoria.TLabel")
        label_categoria2.grid(row=0, sticky='ew')
        label_nombre2=ttk.Label(self.w_happening_but2, text='Como conseguir novia', style='Nombre.TLabel')
        label_nombre2.grid(row=1, sticky='ew')
        label_cantidad2 = ttk.Label(self.w_happening_but2, text='344 mil posts', style="Cantidad.TLabel")
        label_cantidad2.grid(row=2, sticky='ew')

        label_categoria3 = ttk.Label(self.w_happening_but3, text='Política', style="Categoria.TLabel")
        label_categoria3.grid(row=0, sticky='ew')
        label_nombre3=ttk.Label(self.w_happening_but3, text='Bombardeen marruecos', style='Nombre.TLabel')
        label_nombre3.grid(row=1, sticky='ew')
        label_cantidad3 = ttk.Label(self.w_happening_but3, text='875 mil posts', style="Cantidad.TLabel")
        label_cantidad3.grid(row=2, sticky='ew')

        label_categoria4 = ttk.Label(self.w_happening_but4, text='Denuncias', style="Categoria.TLabel")
        label_categoria4.grid(row=0, sticky='ew')
        label_nombre4=ttk.Label(self.w_happening_but4, text='juan violador', style='Nombre.TLabel')
        label_nombre4.grid(row=1, sticky='ew')
        label_cantidad4 = ttk.Label(self.w_happening_but4, text='2 millones de posts', style="Cantidad.TLabel")
        label_cantidad4.grid(row=2, sticky='ew')

        label_categoria5 = ttk.Label(self.w_happening_but5, text='Geo-política', style="Categoria.TLabel")
        label_categoria5.grid(row=0, sticky='ew')
        label_nombre5=ttk.Label(self.w_happening_but5, text='Legitimidad estatal Israel', style='Nombre.TLabel')
        label_nombre5.grid(row=1, sticky='ew')
        label_cantidad5 = ttk.Label(self.w_happening_but5, text='122 mil posts', style="Cantidad.TLabel")
        label_cantidad5.grid(row=2, sticky='ew')


        self.mostrar_mas = ttk.Button(frame_w_happening, text='Mostrar más', style="mostrarMas.TButton", command=self.explorar)
        self.mostrar_mas.grid(row=13, column=0, padx=30, pady=5, sticky='ew')



        categoria = "Educación"
        nombre = "Porno furro"
        cantidad = "500 mil posts"

        self.follow_label = ttk.Label(frame_follow, text='A quién seguir', style='Verification.TLabel')
        self.follow_label.grid(column=0,row=0, padx=50, sticky='ew')

        self.hitler = tk.Button(self.frame_hitler, image=self.hitler_img)
        self.hitler.grid(row=0, sticky='ew', column=0, rowspan=2)

        self.hiltler_label = tk.Label(self.frame_hitler, text='Hiltler✅', font=label_font2)
        self.hiltler_label.grid(row=0, sticky='ew', column=3, padx=0, pady=0)
        self.hitler_label2 = tk.Label(self.frame_hitler, text='@juden_killer', font=tk_style)
        self.hitler_label2.grid(row=1, sticky='ew', column=3, padx=0, pady=0)
        self.hitler_follow = tk.Button(self.frame_hitler, text='Seguir', compound='right', command=self.pulsar_boton_seguir_hitler)
        self.hitler_follow.grid(row=1, column=5, padx=40, sticky='ew')

        self.KKK = tk.Button(self.frameKKK, image=self.KKK_img, command=self.ventana_emergente_prueba)
        self.KKK.grid(row=0, column=0, sticky='ew', rowspan=2)
        self.KKK_label = tk.Label(self.frameKKK, text='KKK', font=label_font2)
        self.KKK_label.grid(row=0, sticky='ew', column=3, padx=0, pady=0)
        self.KKK_label2 = tk.Label(self.frameKKK, text='@KukuxKlan', font=tk_style)
        self.KKK_label2.grid(row=1, sticky='ew', column=3, padx=0, pady=0)
        self.KKK_follow = tk.Button(self.frameKKK, text='Seguir', command=self.pulsar_boton_seguir_kkk)
        self.KKK_follow.grid(row=1, column=5, padx=40, sticky='ew')

        self.generic_doll = tk.Button(self.frame_generic_doll,  command=self.ventana_emergente_prueba)
        self.generic_doll.grid(row=0, column=0, sticky='ew', rowspan=2)
        self.generic_doll_label = tk.Label(self.frame_generic_doll, text='generic_doll✅', font=label_font2)
        self.generic_doll_label.grid(row=0, sticky='ew', column=3, padx=0, pady=0)
        self.generic_doll_label2 = tk.Label(self.frame_generic_doll, text='@generic_doll_official', font=tk_style)
        self.generic_doll_label2.grid(row=1, sticky='ew', column=3, padx=0, pady=0)
        self.generic_doll_follow = tk.Button(self.frame_generic_doll, text='Seguir', command=self.pulsar_boton_seguir_generic_doll)
        self.generic_doll_follow.grid(row=1, column=5, padx=40, sticky='ew')

        self.browser = tk.Button(self.frame_browser,  command=self.ventana_emergente_prueba)
        self.browser.grid(row=0, column=0, sticky='ew', rowspan=2)
        self.browser_label = tk.Label(self.frame_browser, text='browser✅', font=label_font2)
        self.browser_label.grid(row=0, sticky='ew', column=3, padx=0, pady=0)
        self.browser_label2 = tk.Label(self.frame_browser, text='@browser', font=tk_style)
        self.browser_label2.grid(row=1, sticky='ew', column=3, padx=0, pady=0)
        self.browser_follow = tk.Button(self.frame_browser, text='Seguir', command=self.pulsar_boton_seguir_browser)
        self.browser_follow.grid(row=1, column=5, padx=40, sticky='ew')

    #MARK: FUNCIONES
    
    def entry_focus_in(self, event):
        if self.entry_var.get() == self.place_holder_text:
            self.entry_var.set("")
        

    def on_entry_focus_out(self, event):
        if self.entry_var.get() == "":
            self.entry_var.set(self.place_holder_text)
        
    

    def para_ti(self):
        self.estilo_para_ti23452353252345235 = Font(family='Berlin Sans FB', size=14, weight='bold')
        self.estilo_siguiendo223453523452355 = Font(family='Berlin Sans FB', size=14)
        try:
            self.para_ti_button.config(font=self.estilo_para_ti23452353252345235)
            self.siguiendo_button.config(font=self.estilo_siguiendo223453523452355)
        except:
            print(' ')
            print('AÑWFJÑASDKFJKÑASODFJAÑSODKJSAÑFJKASDFJASÑDFJDSAFSJÑD')
        try:

            self.frame_para_ti.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_para_ti')
        try:
            self.frame_para_ti2.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_para_ti2')
        try:
            print(' ')
            self.frame_siguiendo2.destroy()
        except:
            print('INFO: no se ha encontrado self.frame_siguiendo2')
        
        try:
            self.aviso_home.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.aviso_home')
        try:
            self.frame_explorar.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.explorar')
        try:
            self.frame_categorias_titulo_config_notificaciones.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_categorias_titulo_config_notificacion')
        try:
            self.frame_usuarios_para_mensagear.destroy()
        except:
            print(' ')
            print('INFO: self.frame_usuarios_para_mensagear not found')
        try:
            self.frame_chat_hitler.destroy()
        except:
            print('INFO: self.frame_chat_hitler not found')
        self.frame_para_ti2 = ttk.LabelFrame(self.posts_frame)
        self.frame_para_ti2.grid(row=1, column=0, padx=0 , pady=0, sticky='ns')
        

        

        frame_escribir_post = ttk.LabelFrame(self.frame_para_ti2)
        frame_escribir_post.grid(row=0, column=0, pady=0, padx=0, sticky='ew')

        frame_post_airstrike_company = ttk.LabelFrame(self.frame_para_ti2)
        frame_post_airstrike_company.grid(row=1, column=0, pady=0, padx=0, sticky='ew')

        frame_post1 = ttk.LabelFrame(self.frame_para_ti2)
        frame_post1.grid(row=2, column=0, pady=0, padx=0, sticky='ew')

        


        
        
        pad_invisible2 = ttk.Label(self.frame_para_ti2)
        pad_invisible2.grid(padx=710, pady=700)
        pad_invisible2.configure(state='disabled')
        #publicar post
        foto_escribir_post = ttk.Label(frame_escribir_post, image=self.profile2_img)
        foto_escribir_post.grid(row=0, column=0, padx=10, pady=0)
        self.entry_escribir_post = ttk.Entry(frame_escribir_post)
        self.entry_escribir_post.grid(row=0, column=1, padx=0, pady=20, sticky='ew')
        pad_escribir_post_invisible = tk.Label(self.entry_escribir_post)
        pad_escribir_post_invisible.grid(padx=680, pady=0)
        pad_escribir_post_invisible.configure(state='disabled')
        self.boton_publicar_post = ttk.Button(frame_escribir_post, image=self.flechita_img, style='Custom.TButton', command=self.publicar_post)
        self.boton_publicar_post.grid(row=0, column=2, padx=0, pady=0)

        #airstrike_company
        post_foto_airstrike_company = ttk.Label(frame_post_airstrike_company)
        post_foto_airstrike_company.grid(row=0, rowspan=2, column=0, pady=3, padx=5)
        post_nombre_airstrike_company = ttk.Label(frame_post_airstrike_company, text='airstrike_company', style='Nombree.TLabel')
        post_nombre_airstrike_company.grid(row=0, column=1, padx=0, pady=0)
        post_nombre2_airstrike_company = ttk.Label(frame_post_airstrike_company, text='@airstrike_company_oficial', style='Usuario.TLabel')
        post_nombre2_airstrike_company.grid(row=0, column=2, padx=0, pady=0)
        post_airstrike_company = ttk.Label(frame_post_airstrike_company, text='----') 
        post_airstrike_company.grid(row=1, column=1)
        post_airstrike_company2 = ttk.Label(frame_post_airstrike_company, text='¡Prueba nuestro nuevo software para lanzar misiles balisticos desde nuestros increibles satelites nucleares!\n Tan solo pulsa el botón para abrirlo y bombardea a quien quieras (solo para personas autorizadas).')
        post_airstrike_company2.grid(row=1, column=3)
        post_airstrike_company3 = ttk.Label(frame_post_airstrike_company, text='----------->')
        post_airstrike_company3.grid(row=1, column=2)
        balistick_rocket_button = ttk.Button(frame_post_airstrike_company, text='airstrike_company ballistic rocket launching softwar', command=airstrike_company_balistik)
        balistick_rocket_button.grid(row=1, column=4, padx=30)

        post1_foto = ttk.Label(frame_post1, image=self.post1_img)
        post1_foto.grid(row=0, rowspan=2, column=0, pady=3, padx=5)
        post1_nombre = ttk.Label(frame_post1, text='Usuario', style='Nombree.TLabel')
        post1_nombre.grid(row=0, column=1, padx=0, pady=0)
        post1_usuario = ttk.Label(frame_post1, text='@usuario', style='Usuario.TLabel')
        post1_usuario.grid(row=0, column=2, padx=0, pady=0)
        post1 = ttk.Label(frame_post1, text='-------')
        post1.grid(row=1, column=1)
        post1_2 = ttk.Label(frame_post1, text='------->')
        post1_2.grid(row=1, column=2)
        post1_real = ttk.Label(frame_post1, text='Esto es un post')
        post1_real.grid(row=1, column=3)

         
    def publicar_post(self,): 
           # Crear un nuevo frame para el post
        try: #try to insert the post in the frame_para_ti
            new_post_frame = ttk.Frame(self.frame_para_ti)
            new_post_frame.grid(row=self.next_row_of_post, column=1, pady=0, sticky='ew')
            print('INFO: post will spawn in the frame_para_ti')
        except: #if the code above fails, insert the post in the frame_para_ti2
            new_post_frame = ttk.Frame(self.frame_para_ti2)
            new_post_frame.grid(row=self.next_row_of_post, column=1, pady=0, sticky='ew')
            print('INFO: post will spawn in the frame_para_ti2')

        self.new_post_img = ttk.Label(new_post_frame, image=self.post1_img)
        self.new_post_img.grid(row=0, rowspan=2, column=0, pady=3, padx=5)
        self.new_post_name = ttk.Label(new_post_frame, text=self.nombre_usuario_publico, style='Nombree.TLabel')
        self.new_post_name.grid(row=0, column=1, padx=0, pady=0)
        self.new_post_user = ttk.Label(new_post_frame, text=self.nombre_usuario_publico +'@', style='Usuario.TLabel')
        self.new_post_user.grid(row=0, column=2, padx=0, pady=0)
        self.new_post_tecnical_uses_text = ttk.Label(new_post_frame, text='-------')
        self.new_post_tecnical_uses_text.grid(row=1, column=1)
        self.new_post_tecnical_uses_text2 = ttk.Label(new_post_frame, text='------->')
        self.new_post_tecnical_uses_text2.grid(row=1, column=2)
        try:
            text_of_the_post = self.entry_escribir_post.get()
        except:
            pass
        self.new_post = ttk.Label(new_post_frame, text=text_of_the_post) 
        self.new_post.grid(row=1, column=3)
        
        # Incrementar el contador de posts publicados
        self.next_row_of_post += 1
        print('next post will spawn in row: ',self.next_row_of_post)
         

        
    #MARK: HOME Y DERIBADOS
    def home_boton(self):
        self.estilo_siguiendo241234 = Font(family='Berlin Sans FB', size=14)
        self.estilo_para_ti24523454 = Font(family='Berlin Sans FB', size=14, weight='bold')
        self.try_to_destroy_standar() #acordarse de la existencia de esto

        if True == False:
            pass
        else:
            self.frame_para_ti_o_siguiendo = ttk.LabelFrame(self.posts_frame, text='INICIO')
            self.frame_para_ti_o_siguiendo.grid(row=0, column=0,sticky='ew')

            self.estilo_para_ti1 = Font(family='Berlin Sans FB', size=14)
            self.estilo_siguiendo1 = Font(family='Berlin Sans FB', size=14)
            self.para_ti_button = tk.Button(self.frame_para_ti_o_siguiendo, text='Para ti', command=self.para_ti, font=self.estilo_para_ti1)
            self.para_ti_button.grid(row=0, column=0, padx=315, sticky='ew')
            self.siguiendo_button = tk.Button(self.frame_para_ti_o_siguiendo, text='Siguiendo', command=self.siguiendo, font=self.estilo_siguiendo1)
            self.siguiendo_button.grid(row=0, column=1, padx=315, sticky='ew')
            

        
        self.aviso_home = ttk.Label(self.posts_frame, text='selecciona una categoria para verla')
        self.aviso_home.grid(row=1, column=0, pady=200, padx=625, sticky='ew')
        
    def ventana_emergente_prueba(self):
        self.try_to_destroy_ventanas()
        self.ventana_emergente = tk.Toplevel(window)
        funcion_en_desarrollo = ttk.Label(self.ventana_emergente, text='funcion en desarrollo.')
        funcion_en_desarrollo.pack()

    def pulsar_boton_seguir_hitler(self):
        self.siguiendo_hitler = True

        self.hitler_follow.destroy()
        self.hitler_actually_following = tk.Button(self.frame_hitler, text='siguiendo', compound='right',command=self.pulsar_boton_siguiendo_hitler)
        self.hitler_actually_following.grid(row=1, column=5, padx=40, sticky='ew')
    def pulsar_boton_siguiendo_hitler(self):
        self.siguiendo_hitler = False

        self.hitler_actually_following.destroy()
        self.hitler_follow = tk.Button(self.frame_hitler, text='Seguir', compound='right', command=self.pulsar_boton_seguir_hitler)
        self.hitler_follow.grid(row=1, column=5, padx=40, sticky='ew')

    
    def pulsar_boton_seguir_kkk(self):
        self.siguiendo_kkk = True

        self.KKK_follow.destroy()
        self.kkk_actually_following = tk.Button(self.frameKKK, text='siguiendo', compound='right',command=self.pulsar_boton_siguiendo_kkk)
        self.kkk_actually_following.grid(row=1, column=5, padx=40, sticky='ew')
    def pulsar_boton_siguiendo_kkk(self):
        self.siguiendo_kkk = False
        
        self.kkk_actually_following.destroy()
        self.KKK_follow = tk.Button(self.frameKKK, text='Seguir', compound='right', command=self.pulsar_boton_seguir_kkk)
        self.KKK_follow.grid(row=1, column=5, padx=40, sticky='ew')

    def pulsar_boton_seguir_generic_doll(self):
        self.siguiendo_generic_doll = True

        self.generic_doll_follow.destroy()
        self.generic_doll_actually_following = tk.Button(self.frame_generic_doll, text='siguiendo', compound='right',command=self.pulsar_boton_siguiendo_generic_doll)
        self.generic_doll_actually_following.grid(row=1, column=5, padx=40, sticky='ew')
    def pulsar_boton_siguiendo_generic_doll(self):
        self.siguiendo_generic_doll = False
        
        self.generic_doll_actually_following.destroy()
        self.generic_doll_follow = tk.Button(self.frame_generic_doll, text='Seguir', compound='right', command=self.pulsar_boton_seguir_generic_doll)
        self.generic_doll_follow.grid(row=1, column=5, padx=40, sticky='ew')
        
    def pulsar_boton_seguir_browser(self):
        self.siguiendo_browser = True

        self.browser_follow.destroy()
        self.browser_actually_following = tk.Button(self.frame_browser, text='siguiendo', compound='right',command=self.pulsar_boton_siguiendo_browser)
        self.browser_actually_following.grid(row=1, column=5, padx=40, sticky='ew')
    def pulsar_boton_siguiendo_browser(self):
        
        self.siguiendo_browser = False
        
        self.browser_actually_following.destroy()
        self.browser_follow = tk.Button(self.frame_browser, text='Seguir', compound='right', command=self.pulsar_boton_seguir_browser)
        self.browser_follow.grid(row=1, column=5, padx=40, sticky='ew')
        
    #MARK: SIGUIENDO Y DERIVADOS
    def siguiendo(self):
        self.estilo_siguiendo24123 = Font(family='Berlin Sans FB', size=14, weight='bold')
        self.estilo_para_ti2452345 = Font(family='Berlin Sans FB', size=14)
        try:
            self.siguiendo_button.config(font=self.estilo_siguiendo24123)
            self.para_ti_button.config(font=self.estilo_para_ti2452345)
        except:
            print(' ')
            print('JODEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR')
        
        try:

            self.frame_para_ti.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_para_ti')
        try:
            self.frame_para_ti2.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_para_ti2')
        try:
            print(' ')
            self.frame_siguiendo2.destroy()
        except:
            print('INFO: no se ha encontrado self.frame_siguiendo2')
        
        try:
            self.aviso_home.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.aviso_home')

            
        
        self.frame_siguiendo2 = ttk.LabelFrame(self.posts_frame,)
        self.frame_siguiendo2.grid(row=1, column=0, padx=0 , pady=0, sticky='ns')

        self.espaciado_invisible_siguiendo2 = ttk.Label(self.frame_siguiendo2)
        self.espaciado_invisible_siguiendo2.grid(row=29, column=0, sticky='ew', padx=705, pady=0)
        self.espaciado_invisible_siguiendo2.config(state='disabled')
        
        
        try:
            if self.siguiendo_hitler == True:
                self.frame_post_hitler = ttk.LabelFrame(self.frame_siguiendo2)
                self.frame_post_hitler.grid(row=0, column=0, padx=0, pady=0, sticky='ew')

                post_hitler_foto = ttk.Label(self.frame_post_hitler, image=self.hitler_img)
                post_hitler_foto.grid(row=0, rowspan=2, column=0, pady=3, padx=5)
                post_hitler_nombre = ttk.Label(self.frame_post_hitler, text='Hitler', style='Nombree.TLabel')
                post_hitler_nombre.grid(row=0, column=1, padx=0, pady=0)
                post_hitler_usuario = ttk.Label(self.frame_post_hitler, text='@juden_killer', style='Usuario.TLabel')
                post_hitler_usuario.grid(row=0, column=2, padx=0, pady=0)
                post_hitler = ttk.Label(self.frame_post_hitler, text='-------')
                post_hitler.grid(row=1, column=1)
                post_hitler_2 = ttk.Label(self.frame_post_hitler, text='------->')
                post_hitler_2.grid(row=1, column=2)
                post_hitler_real = ttk.Label(self.frame_post_hitler, text='hoy polonia ha sido invadida por nuestras increibles tropas, heil hitler 🤚')
                post_hitler_real.grid(row=1, column=3)
        except:
            print(' ')
            print('INFO: no se ha encontrado self.siguiendo_hitler')
        try:
            if self.siguiendo_kkk == True:
                self.frame_post_kkk = ttk.LabelFrame(self.frame_siguiendo2)
                self.frame_post_kkk.grid(row=1, column=0, padx=0, pady=0, sticky='ew')

                post_kkk_foto = ttk.Label(self.frame_post_kkk, image=self.KKK_img)
                post_kkk_foto.grid(row=0, rowspan=2, column=0, pady=3, padx=5)
                post_kkk_nombre = ttk.Label(self.frame_post_kkk, text='KKK', style='Nombree.TLabel')
                post_kkk_nombre.grid(row=0, column=1, padx=0, pady=0)
                post_kkk_usuario = ttk.Label(self.frame_post_kkk, text='@KuKuxKlan', style='Usuario.TLabel')
                post_kkk_usuario.grid(row=0, column=2, padx=0, pady=0)
                post_kkk = ttk.Label(self.frame_post_kkk, text='-------')
                post_kkk.grid(row=1, column=1)
                post_kkk_2 = ttk.Label(self.frame_post_kkk, text='------->')
                post_kkk_2.grid(row=1, column=2)
                post_kkk_real = ttk.Label(self.frame_post_kkk, text='I hate niggers 🤖')
                post_kkk_real.grid(row=1, column=3)
        except:
            print(' ')
            print('INFO: no se ha encontrado self.siguiendo_kkk')
        try:
            if self.siguiendo_generic_doll == True:
                self.frame_post_generic_doll = ttk.LabelFrame(self.frame_siguiendo2)
                self.frame_post_generic_doll.grid(row=2, column=0, padx=0, pady=0, sticky='ew')

                post_generic_doll_foto = ttk.Label(self.frame_post_generic_doll,)
                post_generic_doll_foto.grid(row=0, rowspan=2, column=0, pady=3, padx=5)
                post_generic_doll_nombre = ttk.Label(self.frame_post_generic_doll, text='generic_doll', style='Nombree.TLabel')
                post_generic_doll_nombre.grid(row=0, column=1, padx=0, pady=0)
                post_generic_doll_usuario = ttk.Label(self.frame_post_generic_doll, text='@generic_doll_official', style='Usuario.TLabel')
                post_generic_doll_usuario.grid(row=0, column=2, padx=0, pady=0)
                post_generic_doll = ttk.Label(self.frame_post_generic_doll, text='-------')
                post_generic_doll.grid(row=1, column=1)
                post_generic_doll_2 = ttk.Label(self.frame_post_generic_doll, text='------->')
                post_generic_doll_2.grid(row=1, column=2)
                post_generic_doll_real = ttk.Label(self.frame_post_generic_doll, text='hey chicas nos vamos de viaje a polonia! compra ya la nueva vestimenta de turismo por europa.')
                post_generic_doll_real.grid(row=1, column=3)
        except:
            print(' ')
            print('INFO: no se ha encontrado self.siguiendo_generic_doll')
        try:
            if self.siguiendo_browser == True:
                self.frame_post_generic_doll = ttk.LabelFrame(self.frame_siguiendo2)
                self.frame_post_generic_doll.grid(row=3, column=0, padx=0, pady=0, sticky='ew')

                post_generic_doll_foto = ttk.Label(self.frame_post_generic_doll)
                post_generic_doll_foto.grid(row=0, rowspan=2, column=0, pady=3, padx=5)
                post_generic_doll_nombre = ttk.Label(self.frame_post_generic_doll, text='browser', style='Nombree.TLabel')
                post_generic_doll_nombre.grid(row=0, column=1, padx=0, pady=0)
                post_generic_doll_usuario = ttk.Label(self.frame_post_generic_doll, text='@browser', style='Usuario.TLabel')
                post_generic_doll_usuario.grid(row=0, column=2, padx=0, pady=0)
                post_generic_doll = ttk.Label(self.frame_post_generic_doll, text='-------')
                post_generic_doll.grid(row=1, column=1)
                post_generic_doll_2 = ttk.Label(self.frame_post_generic_doll, text='------->')
                post_generic_doll_2.grid(row=1, column=2)
                post_generic_doll_real = ttk.Label(self.frame_post_generic_doll, text='Nueva actualización de generic browser. Se ha añadido browser AI, un mod para deprabados sexuales que gira entorno a la mascota anime de nuestra marca (tambien con variantes hentai)')
                post_generic_doll_real.grid(row=1, column=3)
        except:
            print(' ')
            print('INFO: no se ha encontrado self.siguiendo_browser')
        # try:
        #     if self.siguiendo_hitler and self.siguiendo_generic_doll and self.siguiendo_browser and self.siguiendo_kkk == False:
        #         self.no_sigues_a_nadie = ttk.Label(self.frame_siguiendo2, text='No estas siguiendo a nadie')
        #         self.no_sigues_a_nadie.grid(row=4, column=0, padx=0, pady=0, sticky='ew')
        # except:
        #     print(' ')
        #     print('INFO: no se ha encontrado self.siguiendo_hitler o self.siguiendo_generic_doll o self.siguiendo_browser o self.siguiendo_kkk')
    


    #MARK:EXPLORAR Y DERIBADOS
    def explorar(self): #PONER CATEGORIAS ARRIBA (postS FRAME)
        self.try_to_destroy_standar()
            
        self.frame_explorar = ttk.LabelFrame(self.posts_frame, text='EXPLORAR')
        self.frame_explorar.grid(row=0, column=0, sticky='ns', padx= 0, pady=0)

        

        self.boton_config_explorar = ttk.Button(self.frame_explorar, image=self.config_busqueda_explorar_img, command=self.subventana) 
        self.boton_config_explorar.grid(row=0, column=0, sticky='nsew',padx=0, pady=0)
        

        self.foto_escribir_buscar_explorar = ttk.Label(self.frame_explorar, image=self.profile2_img)
        self.foto_escribir_buscar_explorar.grid(row=0, column=1, padx=10, pady=0)
        self.escribir_buscar_explorar = ttk.Entry(self.frame_explorar)
        self.escribir_buscar_explorar.grid(row=0, column=2, padx=0, pady=20, sticky='ew')
        self.pad_escribir_buscar_invisible_explorar = ttk.Label(self.escribir_buscar_explorar)
        self.pad_escribir_buscar_invisible_explorar.grid(padx=605, pady=0, row=0, column=0)
        self.pad_escribir_buscar_invisible_explorar.config(state='disabled')
        self.boton_enter_explorar = ttk.Button(self.frame_explorar, image=self.flechita_img, command=self.pulsar_boton_buscar_frame_r)
        self.boton_enter_explorar.grid(row=0, column=3, sticky='ew')


        but_w_happening = ttk.Button(self.frame_explorar, style='Padding.TButton')
        but_w_happening.grid(row=1, column=0, padx=0, pady=0, sticky='ew')

        label_categoria1 = ttk.Label(but_w_happening, text='Informática', style="Categoria.TLabel")
        label_categoria1.grid(row=0, sticky='ew', pady=0)
        label_nombre1=ttk.Label(but_w_happening, text='Como conseguir novia', style='Nombre.TLabel')
        label_nombre1.grid(row=1, sticky='ew', pady=0)
        label_cantidad1 = ttk.Label(but_w_happening, text='344 mil posts', style="Cantidad.TLabel")
        label_cantidad1.grid(row=2, sticky='ew', pady=0)

        label_categoria2 = ttk.Label(but_w_happening, text='Informática', style="Categoria.TLabel")
        label_categoria2.grid(row=3, sticky='ew', pady=0)
        label_nombre2=ttk.Label(but_w_happening, text='Como conseguir novia', style='Nombre.TLabel')
        label_nombre2.grid(row=4, sticky='ew', pady=0)
        label_cantidad2 = ttk.Label(but_w_happening, text='344 mil posts', style="Cantidad.TLabel")
        label_cantidad2.grid(row=5, sticky='ew', pady=0)

        label_categoria3 = ttk.Label(but_w_happening, text='Informática', style="Categoria.TLabel")
        label_categoria3.grid(row=6, sticky='ew', pady=0)
        label_nombre3=ttk.Label(but_w_happening, text='Como conseguir novia', style='Nombre.TLabel')
        label_nombre3.grid(row=7, sticky='ew', pady=0)
        label_cantidad3 = ttk.Label(but_w_happening, text='344 mil posts', style="Cantidad.TLabel")
        label_cantidad3.grid(row=8, sticky='ew', pady=0)

        label_categoria4 = ttk.Label(but_w_happening, text='Informática', style="Categoria.TLabel")
        label_categoria4.grid(row=9, sticky='ew', pady=0)
        label_nombre4=ttk.Label(but_w_happening, text='Como conseguir novia', style='Nombre.TLabel')
        label_nombre4.grid(row=10, sticky='ew', pady=0)
        label_cantidad4 = ttk.Label(but_w_happening, text='344 mil posts', style="Cantidad.TLabel")
        label_cantidad4.grid(row=11, sticky='ew', pady=0)

        label_categoria13 = ttk.Label(but_w_happening, text='Informática', style="Categoria.TLabel")
        label_categoria13.grid(row=12, sticky='ew', pady=0)
        label_nombre13 = ttk.Label(but_w_happening, text='Como conseguir novia', style='Nombre.TLabel')
        label_nombre13.grid(row=13, sticky='ew', pady=0)
        label_cantidad13 = ttk.Label(but_w_happening, text='344 mil posts', style="Cantidad.TLabel")
        label_cantidad13.grid(row=14, sticky='ew', pady=0)

        label_categoria16 = ttk.Label(but_w_happening, text='Informática', style="Categoria.TLabel")
        label_categoria16.grid(row=15, sticky='ew', pady=0)
        label_nombre16 = ttk.Label(but_w_happening, text='Como conseguir novia', style='Nombre.TLabel')
        label_nombre16.grid(row=16, sticky='ew', pady=0)
        label_cantidad16 = ttk.Label(but_w_happening, text='344 mil posts', style="Cantidad.TLabel")
        label_cantidad16.grid(row=17, sticky='ew', pady=0)
        self.boton_activado = False
    def subventana(self):
        self.config_busqueda_explorar_ventana = tk.Toplevel(self.wind)
        self.config_busqueda_explorar_ventana.title = ('Configuración de busqueda')
        self.label_ajuste = ttk.Label(self.config_busqueda_explorar_ventana, text='Buscar en base a tu ubicación')
        self.label_ajuste.grid(row=0, sticky='ew', pady=0, padx=0, column=0)
        if self.boton_activado == False:
            self.boton_ajuste = tk.Button(self.config_busqueda_explorar_ventana, text='desactivado', command=self.pulsar_boton_ajuste_busqueda_explorar_ventana)
            self.boton_ajuste.grid(row=0, sticky='ew', column=1, pady=0, padx=0)
        else:
            self.boton_ajuste_activado = tk.Button(self.config_busqueda_explorar_ventana, text='activado', command=self.pulsar_boton_ajuste_busqueda_explorar_ventana_pero_esto_desactiva)
            self.boton_ajuste_activado.grid(row=0, sticky='ew', column=1, pady=0, padx=0)
            self.boton_activado= True
    def pulsar_boton_ajuste_busqueda_explorar_ventana(self):
        
        self.boton_ajuste.destroy()
        self.boton_ajuste_activado = tk.Button(self.config_busqueda_explorar_ventana, text='activado', command=self.pulsar_boton_ajuste_busqueda_explorar_ventana_pero_esto_desactiva)
        self.boton_ajuste_activado.grid(row=0, sticky='ew', column=1, pady=0, padx=0)

        self.boton_activado= True
    
    def pulsar_boton_ajuste_busqueda_explorar_ventana_pero_esto_desactiva(self):
        self.boton_ajuste = tk.Button(self.config_busqueda_explorar_ventana, text='desactivado', command=self.pulsar_boton_ajuste_busqueda_explorar_ventana)
        self.boton_ajuste.grid(row=0, sticky='ew', column=1, pady=0, padx=0)

        self.boton_activado = False

    #MARK: NOTIFICACIONES Y DERIVADOS
    def notificaciones(self):
        self.try_to_destroy_standar()

        
        self.frame_categorias_titulo_config_notificaciones = ttk.LabelFrame(self.posts_frame)
        self.frame_categorias_titulo_config_notificaciones.grid(row= 0, padx=0, sticky='ew', column=0, pady=0)
        self.espaciado_interno_notificaciones = ttk.Label(self.frame_categorias_titulo_config_notificaciones)
        self.espaciado_interno_notificaciones.grid(padx=700, row=1)
        self.espaciado_interno_notificaciones.config(state='disabled')
        


        #ESTILOS
        self.estilo_notis_sin_negrita = Font(family='Berlin Sans FB', size=13)
        self.estilo_notis_negrita = Font(family='Berlin Sans FB', size=13, weight='bold')
        
        #--------------------------
        self.titulo_label_notificaciones = ttk.Label(self.frame_categorias_titulo_config_notificaciones, text='Notificaciones', style="Custom.TLabel")
        self.titulo_label_notificaciones.grid(row= 0, padx=0, sticky='ew', column=0, pady=0)
        self.config_notificaciones = ttk.Button(self.frame_categorias_titulo_config_notificaciones, image=self.config_busqueda_explorar_img, command=self.pulsar_boton_ajuste_notis)
        self.frame_todas_notis_verificado_o_menciones = ttk.LabelFrame(self.frame_categorias_titulo_config_notificaciones)
        self.frame_todas_notis_verificado_o_menciones.grid(row= 3, column=0, padx=0, pady=0, sticky='ew', columnspan=3)
        self.config_notificaciones.grid(row= 0, column=2, padx=0, pady=0, sticky='ew')

        self.todas_notificaciones = tk.Button(self.frame_todas_notis_verificado_o_menciones, text='Todas', font=self.estilo_notis_sin_negrita, command=self.pulsar_boton_todas_notificaciones, padx=200)
        self.todas_notificaciones.config()
        self.todas_notificaciones.grid(row=0, column=0, padx=0, sticky='ew', pady=0, )
        self.verificado_notificaciones = tk.Button(self.frame_todas_notis_verificado_o_menciones, text='Verificado', font=self.estilo_notis_sin_negrita, command=self.pulsar_boton_verificado_notificaciones, padx=200)
        self.verificado_notificaciones.config()
        self.verificado_notificaciones.grid(row=0, column=1, padx=0, sticky='ew', pady=0,)
        self.menciones_notificaciones = tk.Button(self.frame_todas_notis_verificado_o_menciones, text='Menciones', font=self.estilo_notis_sin_negrita, command=self.pulsar_boton_menciones_notificaciones, padx=200)
        self.menciones_notificaciones.config()
        self.menciones_notificaciones.grid(row=0, column=2, padx=0, sticky='ew', pady=0)

        
        self.aviso_home = ttk.Label(self.posts_frame, text='selecciona una categoria para verla')
        self.aviso_home.grid(row=1, column=0, pady=200, padx=625, sticky='ew')
        
    def pulsar_boton_todas_notificaciones(self):
        self.todas_notificaciones.config(font=self.estilo_notis_negrita)
        self.verificado_notificaciones.config(font=self.estilo_notis_sin_negrita)
        self.menciones_notificaciones.config(font=self.estilo_notis_sin_negrita)

        try:
            self.frame_noti_hitler.destroy()
        except:
            print('INFO: self.frame_noti_hitler not found')
        try:
            self.frame_noti_hacienda.destroy()
        except:
            print('INFO: self.frame_noti_hacienda not found')
        try:
            self.frame_noti_social_media_app_simulator.destroy()
        except:
            print('INFO: self.frame_noti_social_media_app_simulator not found')
        
        self.frame_noti_hitler = ttk.LabelFrame(self.frame_categorias_titulo_config_notificaciones)
        self.frame_noti_hitler.grid(row=4, column=0, sticky='ew', padx=0, pady=0)

        post_hitler_foto = ttk.Label(self.frame_noti_hitler, image=self.hitler_img)
        post_hitler_foto.grid(row=0, rowspan=2, column=0, pady=3, padx=5)
        post_hitler_nombre = ttk.Label(self.frame_noti_hitler, text='Hitler✅', style='Nombree.TLabel')
        post_hitler_nombre.grid(row=0, column=1, padx=0, pady=0)
        post_hitler_usuario = ttk.Label(self.frame_noti_hitler, text='@juden_killer', style='Usuario.TLabel')
        post_hitler_usuario.grid(row=0, column=2, padx=0, pady=0)
        post_hitler = ttk.Label(self.frame_noti_hitler, text='-------')
        post_hitler.grid(row=1, column=1)
        post_hitler_2 = ttk.Label(self.frame_noti_hitler, text='------->')
        post_hitler_2.grid(row=1, column=2)

        self.frame_noti_hacienda = ttk.LabelFrame(self.frame_categorias_titulo_config_notificaciones)
        self.frame_noti_hacienda.grid(row=6, column=0, sticky='ew', padx=0, pady=0)

        post_hacienda_foto = ttk.Label(self.frame_noti_hacienda)
        post_hacienda_foto.grid(row=0, rowspan=2, column=0, pady=3, padx=5)
        post_hacienda_nombre = ttk.Label(self.frame_noti_hacienda, text='Hacienda', style='Nombree.TLabel')
        post_hacienda_nombre.grid(row=0, column=1, padx=0, pady=0)
        post_hacienda_usuario = ttk.Label(self.frame_noti_hacienda, text='@los_ladrones', style='Usuario.TLabel')
        post_hacienda_usuario.grid(row=0, column=2, padx=0, pady=0)
        post_hacienda = ttk.Label(self.frame_noti_hacienda, text='-------')
        post_hacienda.grid(row=1, column=1)
        post_hacienda_2 = ttk.Label(self.frame_noti_hacienda, text='------->')
        post_hacienda_2.grid(row=1, column=2)
        self.post_hacienda_real_menciones = ttk.Label(self.frame_noti_hacienda, text=(self.nombre_usuario_publico, 'hello world'))
        self.post_hacienda_real_menciones.grid(row=1, column=3)
        if self.boton_pulsado_menciones == False:
            self.post_hacienda_silenciar_menciones = ttk.Button(self.post_hacienda_real_menciones, text='silenciar', command=self.pulsar_boton_silenciar_notis_menciones)
            self.post_hacienda_silenciar_menciones.grid(row=0, column=1, padx=280, pady=0, sticky='ew')
        elif self.boton_pulsado_menciones == True:
            self.post_hacienda_silenciar_menciones_activado = ttk.Button(self.post_hacienda_real_menciones, text='silenciado', command=self.pulsar_boton_silenciar_notis_menciones_activ)
            self.post_hacienda_silenciar_menciones_activado.grid(row=0, column=1, padx=280, pady=0, sticky='ew')
        
        self.post_hitler_real_verificado = ttk.Label(self.frame_noti_hitler, text='hoy polonia ha sido invadida por nuestras increibles tropas, heil hitler 🤚')
        self.post_hitler_real_verificado.grid(row=1, column=3)
        if self.boton_pulsado_verificado == False:
            
            self.post_hitler_silenciar_verificado = ttk.Button(self.post_hitler_real_verificado, text='silenciar', command=self.pulsar_boton_silenciar_notis_verificado)
            self.post_hitler_silenciar_verificado.grid(row=0, column=1, padx=400, pady=0, sticky='ew')
        elif self.boton_pulsado_verificado == True:
            
            self.post_hitler_silenciar_verificado_activado = ttk.Button(self.post_hitler_real_verificado, text='silenciado', command=self.pulsar_boton_silenciar_notis_verificado_activ)
            self.post_hitler_silenciar_verificado_activado.grid(row=0, column=1, padx=400, pady=0, sticky='ew')

        self.frame_noti_social_media_app_simulator = ttk.LabelFrame(self.frame_categorias_titulo_config_notificaciones)
        self.frame_noti_social_media_app_simulator.grid(row=5, column=0, sticky='ew', padx=0, pady=0)

        post_social_media_app_simulator_foto = ttk.Label(self.frame_noti_social_media_app_simulator)
        post_social_media_app_simulator_foto.grid(row=0, rowspan=2, column=0, pady=3, padx=5)
        post_social_media_app_simulator_nombre = ttk.Label(self.frame_noti_social_media_app_simulator, text='social_media_app_simulator', style='Nombree.TLabel')
        post_social_media_app_simulator_nombre.grid(row=0, column=1, padx=0, pady=0)
        post_social_media_app_simulator_usuario = ttk.Label(self.frame_noti_social_media_app_simulator, text='@social_media_app_simulator', style='Usuario.TLabel')
        post_social_media_app_simulator_usuario.grid(row=0, column=2, padx=0, pady=0)
        post_social_media_app_simulator = ttk.Label(self.frame_noti_social_media_app_simulator, text='-------')
        post_social_media_app_simulator.grid(row=1, column=1)
        post_social_media_app_simulator_2 = ttk.Label(self.frame_noti_social_media_app_simulator, text='------->')
        post_social_media_app_simulator_2.grid(row=1, column=2)
        self.post_social_media_app_simulator_real = ttk.Label(self.frame_noti_social_media_app_simulator, text='Se ha iniciado sesión en tu cuenta Usuario desde un dispositivo nuevo el 28 ago. 2023. Compruébalo ahora.')
        self.post_social_media_app_simulator_real.grid(row=1, column=3)
        

        if self.boton_pulsado_social_media_app_simulator == False:
            self.post_social_media_app_simulator_silenciar_social_media_app_simulator = ttk.Button(self.post_social_media_app_simulator_real, text='silenciar', command=self.pulsar_boton_silenciar_notis_social_media_app_simulator)
            self.post_social_media_app_simulator_silenciar_social_media_app_simulator.grid(row=0, column=1, padx=580, pady=0, sticky='ew')
        elif self.boton_pulsado_social_media_app_simulator == True:
            self.post_social_media_app_simulator_silenciar_social_media_app_simulator_activado = ttk.Button(self.post_social_media_app_simulator_real, text='silenciado', command=self.pulsar_boton_silenciar_notis_social_media_app_simulator_activ)
            self.post_social_media_app_simulator_silenciar_social_media_app_simulator_activado.grid(row=0, column=1, padx=580, pady=0, sticky='ew')
        
    

    def pulsar_boton_silenciar_notis_social_media_app_simulator(self):
        try:
            self.post_social_media_app_simulator_silenciar_social_media_app_simulator.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.post_social_media_app_simulator_silenciar_social_media_app_simulator')
        try:
            self.post_social_media_app_simulator_silenciar_social_media_app_simulator_activado.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.post_social_media_app_simulator_silenciar_social_media_app_simulator_activado')
        self.boton_pulsado_social_media_app_simulator = True
        if self.boton_pulsado_social_media_app_simulator == True:
            try:
                self.postsocial_media_app_simulator_silenciar_social_media_app_simulator_activado = ttk.Button(self.post_social_media_app_simulator_real, text='silenciado', command=self.pulsar_boton_silenciar_notis_social_media_app_simulator_activ)
                self.postsocial_media_app_simulator_silenciar_social_media_app_simulator_activado.grid(row=0, column=1, padx=580, pady=0, sticky='ew')
            except:
                print(' ')
                print('INFO: no such self.post_social_media_app_simulator_real or ventana')
            try:
                self.config_social_media_app_simulator_button = tk.Button(self.frame_notis_config_social_media_app_simulator, command=self.pulsar_boton_silenciar_notis_social_media_app_simulator_activ, text='silenciado')
                self.config_social_media_app_simulator_button.grid(row=0, column=3, padx=10, pady=0, sticky='ew')
            except:
                print(' ')
                print('INFO: no such self.frame_notis_config_social_media_app_simulator or ventana')

    def pulsar_boton_silenciar_notis_social_media_app_simulator_activ(self):
        try:
            self.post_social_media_app_simulator_silenciar_social_media_app_simulator_activado.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.postsocial_media_app_simulator_silenciar_social_media_app_simulator_activado')
        try:
            self.post_social_media_app_simulator_silenciar_social_media_app_simulator.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.post_social_media_app_simulator_silenciar_social_media_app_simulator')
        self.boton_pulsado_social_media_app_simulator = False
        if self.boton_pulsado_social_media_app_simulator == False:
            try:
                self.post_social_media_app_simulator_silenciar_social_media_app_simulator = ttk.Button(self.post_social_media_app_simulator_real, text='silenciar', command=self.pulsar_boton_silenciar_notis_social_media_app_simulator)
                self.post_social_media_app_simulator_silenciar_social_media_app_simulator.grid(row=0, column=1, padx=580, pady=0, sticky='ew')
            except:
                print(' ')
                print('INFO:o such self.post_social_media_app_simulator_real or ventana')
        
            try:
                self.config_social_media_app_simulator_button = tk.Button(self.frame_notis_config_social_media_app_simulator, command=self.pulsar_boton_silenciar_notis_social_media_app_simulator, text='silenciar')
                self.config_social_media_app_simulator_button.grid(row=0, column=3, padx=10, pady=0, sticky='ew')
            except:
                print(' ')
                print('INFO: no such self.frame_notis_config_social_media_app_simulator_activado or ventana')


                  

        


        

    def pulsar_boton_verificado_notificaciones(self):
        
        self.todas_notificaciones.config(font=self.estilo_notis_sin_negrita)
        self.verificado_notificaciones.config(font=self.estilo_notis_negrita)
        self.menciones_notificaciones.config(font=self.estilo_notis_sin_negrita)
        
        try:
            self.aviso_home.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.aviso_home')
        try:
            self.frame_noti_social_media_app_simulator.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_noti_social_media_app_simulator')
        
        try:
            self.frame_noti_hacienda.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_noti_hacienda')
        self.frame_noti_hitler = ttk.LabelFrame(self.frame_categorias_titulo_config_notificaciones)
        self.frame_noti_hitler.grid(row=4, column=0, sticky='ew', padx=0, pady=0)

        post_hitler_foto = ttk.Label(self.frame_noti_hitler, image=self.hitler_img)
        post_hitler_foto.grid(row=0, rowspan=2, column=0, pady=3, padx=5)
        post_hitler_nombre = ttk.Label(self.frame_noti_hitler, text='Hitler✅', style='Nombree.TLabel')
        post_hitler_nombre.grid(row=0, column=1, padx=0, pady=0)
        post_hitler_usuario = ttk.Label(self.frame_noti_hitler, text='@juden_killer', style='Usuario.TLabel')
        post_hitler_usuario.grid(row=0, column=2, padx=0, pady=0)
        post_hitler = ttk.Label(self.frame_noti_hitler, text='-------')
        post_hitler.grid(row=1, column=1)
        post_hitler_2 = ttk.Label(self.frame_noti_hitler, text='------->')
        post_hitler_2.grid(row=1, column=2)
        self.post_hitler_real_verificado = ttk.Label(self.frame_noti_hitler, text='hoy polonia ha sido invadida por nuestras increibles tropas, heil hitler 🤚')
        self.post_hitler_real_verificado.grid(row=1, column=3)
        if self.boton_pulsado_verificado == False:
            try:
                self.post_hitler_silenciar_verificado_activado.destroy()
            except:
                print(' ')
                print('INFO: no se ha encontrado self.post_hitler_silenciar_verificado_activado')
            self.post_hitler_silenciar_verificado = ttk.Button(self.post_hitler_real_verificado, text='silenciar', command=self.pulsar_boton_silenciar_notis_verificado)
            self.post_hitler_silenciar_verificado.grid(row=0, column=1, padx=400, pady=0, sticky='ew')
        elif self.boton_pulsado_verificado == True:
            try:
                self.post_hitler_silenciar_verificado.destroy()
            except:
                print(' ')
                print('INFO: no se ha encontrado self.post_hitler_silenciar_verificado')
            self.post_hitler_silenciar_verificado_activado = ttk.Button(self.post_hitler_real_verificado, text='silenciado', command=self.pulsar_boton_silenciar_notis_verificado_activ)
            self.post_hitler_silenciar_verificado_activado.grid(row=0, column=1, padx=400, pady=0, sticky='ew')
        
    
    def pulsar_boton_silenciar_notis_verificado(self):
        try:
            self.post_hitler_silenciar_verificado.destroy()
        except:
            print('INFO: no se ha encontrado self.post_hitler_silenciar_verificado_activado')
        try:
            self.post_hitler_silenciar_verificado_activado.destroy()
        except:
            print(' ')
            print('INFO:o se ha encontrado self.post_hacienda_silenciar_menciones')
        self.boton_pulsado_verificado = True
        if self.boton_pulsado_verificado == True:
            try:
                self.post_hitler_silenciar_verificado_activado = ttk.Button(self.post_hitler_real_verificado, text='silenciado', command=self.pulsar_boton_silenciar_notis_verificado_activ)
                self.post_hitler_silenciar_verificado_activado.grid(row=0, column=1, padx=400, pady=0, sticky='ew')
            except:
                print(' ')
                print('INFO: no such self.post_hitler_real_verificado or ventana')
            try:
                self.notis_config_hitler_button = tk.Button(self.frame_notis_config_hitler, command=self.pulsar_boton_silenciar_notis_verificado_activ, text='silenciado')
                self.notis_config_hitler_button.grid(row=0, column=3, padx=10, pady=0, sticky='ew')
            except:
                print(' ')
                print('INFO: no such self.frame_notis_config_hitler or ventana')


    def pulsar_boton_silenciar_notis_verificado_activ(self):
        try:
             self.post_hitler_silenciar_verificado_activado.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.post_hitler_silenciar_verificado_activado')
        try:
            self.post_hitler_silenciar_verificado.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.post_hacienda_silenciar_menciones')
        self.boton_pulsado_verificado = False
        if self.boton_pulsado_verificado == False:
            try:
                self.post_hitler_silenciar_verificado = ttk.Button(self.post_hitler_real_verificado, text='silenciar', command=self.pulsar_boton_silenciar_notis_verificado)
                self.post_hitler_silenciar_verificado.grid(row=0, column=1, padx=400, pady=0, sticky='ew')
            except:
                print(' ')
                print('no such self.post_hitler_real_verificado or ventana')
            try:
                self.notis_config_hitler_button = tk.Button(self.frame_notis_config_hitler, command=self.pulsar_boton_silenciar_notis_verificado, text='silenciar')
                self.notis_config_hitler_button.grid(row=0, column=3, padx=10, pady=0, sticky='ew')
            except:
                print(' ')
                print('INFO: no such self.frame_notis_config_hitler or ventana')

    def pulsar_boton_menciones_notificaciones(self):
        
        self.todas_notificaciones.config(font=self.estilo_notis_sin_negrita)
        self.verificado_notificaciones.config(font=self.estilo_notis_sin_negrita)
        self.menciones_notificaciones.config(font=self.estilo_notis_negrita)

        
        try:
            self.aviso_home.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.aviso_home')
        try:
            self.frame_explorar.destroy()
        except:
            print(' ')
            print('INFO:no se ha encontrado self.explorar')
        
        try:
            self.frame_noti_social_media_app_simulator.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_noti_social_media_app_simulator')
        try:
            self.frame_noti_hitler.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_noti_hitler')
        try:
            self.frame_noti_hacienda.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_noti_hacienda')

        
        self.frame_noti_hacienda = ttk.LabelFrame(self.frame_categorias_titulo_config_notificaciones)
        self.frame_noti_hacienda.grid(row=4, column=0, sticky='ew', padx=0, pady=0)

        post_hacienda_foto = ttk.Label(self.frame_noti_hacienda)
        post_hacienda_foto.grid(row=0, rowspan=2, column=0, pady=3, padx=5)
        post_hacienda_nombre = ttk.Label(self.frame_noti_hacienda, text='hacienda', style='Nombree.TLabel')
        post_hacienda_nombre.grid(row=0, column=1, padx=0, pady=0)
        post_hacienda_usuario = ttk.Label(self.frame_noti_hacienda, text='@los_ladrones', style='Usuario.TLabel')
        post_hacienda_usuario.grid(row=0, column=2, padx=0, pady=0)
        post_hacienda = ttk.Label(self.frame_noti_hacienda, text='-------')
        post_hacienda.grid(row=1, column=1)
        post_hacienda_2 = ttk.Label(self.frame_noti_hacienda, text='------->')
        post_hacienda_2.grid(row=1, column=2)
        self.post_hacienda_real_menciones = ttk.Label(self.frame_noti_hacienda, text=(self.nombre_usuario_publico, 'hello world'))
        self.post_hacienda_real_menciones.grid(row=1, column=3)
        if self.boton_pulsado_menciones == False:
            self.post_hacienda_silenciar_menciones = ttk.Button(self.post_hacienda_real_menciones, text='silenciar', command=self.pulsar_boton_silenciar_notis_menciones)
            self.post_hacienda_silenciar_menciones.grid(row=0, column=1, padx=280, pady=0, sticky='ew')
        elif self.boton_pulsado_menciones == True:
            self.post_hacienda_silenciar_menciones_activado = ttk.Button(self.post_hacienda_real_menciones, text='silenciado', command=self.pulsar_boton_silenciar_notis_menciones_activ)
            self.post_hacienda_silenciar_menciones_activado.grid(row=0, column=1, padx=280, pady=0, sticky='ew')
        
    

    def pulsar_boton_silenciar_notis_menciones(self):
        try:
            self.post_hacienda_silenciar_menciones.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.post_hacienda_silenciar_menciones')
        try:
            self.post_hacienda_silenciar_menciones_activado.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.post_hacienda_silenciar_mencionesd_activado')
        
        self.boton_pulsado_menciones = True
        if self.boton_pulsado_menciones == True:
            try:
                self.post_hacienda_silenciar_menciones_activado = ttk.Button(self.post_hacienda_real_menciones, text='silenciado', command=self.pulsar_boton_silenciar_notis_menciones_activ)
                self.post_hacienda_silenciar_menciones_activado.grid(row=0, column=1, padx=280, pady=0, sticky='ew')
            except:
                print(' ')
                print('INFO: no such self.post_hacienda-real_menciones or ventana')
            try:
                config_hacienda_button = tk.Button(self.frame_notis_config_hacienda,command=self.pulsar_boton_silenciar_notis_menciones_activ, text='silenciado' )
                config_hacienda_button.grid(row=0, column=3, padx=0, pady=0, sticky='ew')

            except:
                print(' ')
                print('INFO: no such self.frame_notis_config_hacienda or ventana')
            

    def pulsar_boton_silenciar_notis_menciones_activ(self):
        try:
            self.post_hacienda_silenciar_menciones.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.post_hacienda_silenciar_menciones')
        try:
            self.post_hacienda_silenciar_menciones_activado.destroy()
        except:
            print(' ')
            print('INFO:no se ha encontrado self.post_hacienda_silenciar_mencionesd_activado')
        self.boton_pulsado_menciones = False
        if self.boton_pulsado_menciones == False:
            try:
                self.post_hacienda_silenciar_menciones = ttk.Button(self.post_hacienda_real_menciones, text='silenciar', command=self.pulsar_boton_silenciar_notis_menciones)
                self.post_hacienda_silenciar_menciones.grid(row=0, column=1, padx=280, pady=0, sticky='ew')
            except:
                print(' ')
                print('INFO: no such self.post_hacienda_real_menciones_activado or ventana')
            try:
                config_hacienda_button = tk.Button(self.frame_notis_config_hacienda,command=self.pulsar_boton_silenciar_notis_menciones, text='silenciar' )
                config_hacienda_button.grid(row=0, column=3, padx=0, pady=0, sticky='ew')

    
            except:
                print(' ')
                print('INFO: no such self.frame_notis_config_hacienda or ventana')

    def pulsar_boton_ajuste_notis(self):
        self.config_notis = tk.Toplevel(window)
        self.config_notis.title('configuración de notificaciones')

        try:
            self.boton_atras.destroy()
        except:
            print(' ')
            print('INFO: self.boton_atras no ha sido encontrado')
        try:
            self.frame_notis_config_hitler.destroy()
        except:
            print(' ')
            print('INFO: self.frame_notis_config_hitler no ha sido encontrado')
        
        self.titulo_boton_ajuste_notis = ttk.Label(self.config_notis, text='filtro de calidad', style='Verification2.TLabel')
        self.titulo_boton_ajuste_notis.grid(row=0, column=0, padx=0, pady=0,sticky='ew')
        self.cuerpo_boton_ajuste_notis = ttk.Label(self.config_notis, text='Elige excluir contenidos como posts duplicados o automatizados. Esto no se aplica a las notificaciones de las cuentas que sigues o con las que hayas interactuado recientemente.')
        self.cuerpo_boton_ajuste_notis.grid(row=1, column=0, padx=0, pady=0, sticky='ew')
        if self.boton_ajuste_notis_toplevel == True:
            self.boton = tk.Button(self.config_notis, text='activado', command=self.pulsar_boton_ajuste_notis_toplevel_pero_desactiva)
            self.boton.grid(row=1, column=1, padx=0, pady=0, sticky='ew')
        elif self.boton_ajuste_notis_toplevel == False:
            self.boton = tk.Button(self.config_notis, text='desactivado', command=self.pulsar_boton_ajuste_notis_toplevel)
            self.boton.grid(row=1, column=1, padx=0, pady=0, sticky='ew')
        self.titulo2_boton_ajuste_notis = ttk.Label(self.config_notis, text='Notificaciones silenciadas', style='Verification2.TLabel')
        self.titulo2_boton_ajuste_notis.grid(row=2, column=0, padx=0, pady=0, sticky='ew')
        self.boton_titulo2_boton_ajuste_notis = ttk.Button(self.titulo2_boton_ajuste_notis, image=self.flechita_img, command=self.tocar_boton_notificaciones_silenciadas_toplvl)
        self.boton_titulo2_boton_ajuste_notis.grid(row=2, column=1, padx=170, pady=0, sticky='ew')

        
    def pulsar_boton_ajuste_notis_toplevel(self):
        self.boton_ajuste_notis_toplevel = True
        self.boton.destroy()
        self.boton = tk.Button(self.config_notis, text='activado', command=self.pulsar_boton_ajuste_notis_toplevel_pero_desactiva)
        self.boton.grid(row=1, column=1, padx=0, pady=0, sticky='ew')

    def pulsar_boton_ajuste_notis_toplevel_pero_desactiva(self):
        self.boton_ajuste_notis_toplevel = False
        self.boton.destroy()
        self.boton = tk.Button(self.config_notis, text='desactivado', command=self.pulsar_boton_ajuste_notis_toplevel)
        self.boton.grid(row=1, column=1, padx=0, pady=0, sticky='ew')
    
    def tocar_boton_notificaciones_silenciadas_toplvl(self):
        self.titulo_boton_ajuste_notis.destroy()
        self.cuerpo_boton_ajuste_notis.destroy()
        self.boton.destroy()
        self.titulo2_boton_ajuste_notis.destroy()

        self.boton_atras = ttk.Button(self.config_notis, command=self.pulsar_boton_atras, image=self.flechita_inversa_img)
        self.boton_atras.grid(row=0, column=0, padx=0, sticky='ns', pady=0)

        self.frame_notis_config_hitler = ttk.LabelFrame(self.config_notis)
        self.frame_notis_config_hitler.grid(row=1, column=1, padx=0, pady=0, sticky='ew')

        notis_config_hitler_foto = ttk.Label(self.frame_notis_config_hitler, image=self.hitler_img)
        notis_config_hitler_foto.grid(row=0, rowspan=2, column=0, pady=3, padx=5)
        notis_config_hitler_nombre = ttk.Label(self.frame_notis_config_hitler, text='Hitler', style='Nombree.TLabel')
        notis_config_hitler_nombre.grid(row=0, column=1, padx=0, pady=0)
        notis_config_hitler_usuario = ttk.Label(self.frame_notis_config_hitler, text='@juden_killer', style='Usuario.TLabel')
        notis_config_hitler_usuario.grid(row=0, column=2, padx=0, pady=0)
        if  self.boton_pulsado_verificado == True:

            notis_config_hitler_button = tk.Button(self.frame_notis_config_hitler, command=self.pulsar_boton_silenciar_notis_verificado_activ, text='silenciado')
            notis_config_hitler_button.grid(row=0, column=3, padx=10, pady=0, sticky='ew')
        elif  self.boton_pulsado_verificado == False:
            notis_config_hitler_button = tk.Button(self.frame_notis_config_hitler, command=self.pulsar_boton_silenciar_notis_verificado, text='silenciar')
            notis_config_hitler_button.grid(row=0, column=3, padx=10, pady=0, sticky='ew')

        self.frame_notis_config_social_media_app_simulator = ttk.LabelFrame(self.config_notis)
        self.frame_notis_config_social_media_app_simulator.grid(row=2, column=1, padx=0 ,pady=0, sticky='ew')

        config_social_media_app_simulator_foto = ttk.Label(self.frame_notis_config_social_media_app_simulator)
        config_social_media_app_simulator_foto.grid(row=0, rowspan=2, column=0, pady=3, padx=5)
        config_social_media_app_simulator_nombre = ttk.Label(self.frame_notis_config_social_media_app_simulator, text='social_media_app_simulator', style='Nombree.TLabel')
        config_social_media_app_simulator_nombre.grid(row=0, column=1, padx=0, pady=0)
        config_social_media_app_simulator_usuario = ttk.Label(self.frame_notis_config_social_media_app_simulator, text='@social_media_app_simulator', style='Usuario.TLabel')
        config_social_media_app_simulator_usuario.grid(row=0, column=2, padx=0, pady=0)
        if self.boton_pulsado_social_media_app_simulator == True:
            config_social_media_app_simulator_button = tk.Button(self.frame_notis_config_social_media_app_simulator, command=self.pulsar_boton_silenciar_notis_social_media_app_simulator_activ, text='silenciado')
            config_social_media_app_simulator_button.grid(row=0, column=3, padx=10, pady=0, sticky='ew')
        elif self.boton_pulsado_social_media_app_simulator == False:
            config_social_media_app_simulator_button = tk.Button(self.frame_notis_config_social_media_app_simulator, command=self.pulsar_boton_silenciar_notis_social_media_app_simulator, text='silenciar')
            config_social_media_app_simulator_button.grid(row=0, column=3, padx=10, pady=0, sticky='ew')

        self.frame_notis_config_hacienda = ttk.LabelFrame(self.config_notis)
        self.frame_notis_config_hacienda.grid(row=3, column=1, padx=0, pady=0, sticky='ew')

        config_hacienda_foto = ttk.Label(self.frame_notis_config_hacienda)
        config_hacienda_foto.grid(row=0, rowspan=2, column=0, pady=3, padx=5)
        config_hacienda_nombre = ttk.Label(self.frame_notis_config_hacienda, text='Hacienda', style='Nombree.TLabel')
        config_hacienda_nombre.grid(row=0, column=1, padx=0, pady=0)
        config_hacienda_usuario = ttk.Label(self.frame_notis_config_hacienda, text='@los_ladrones', style='Usuario.TLabel')
        config_hacienda_usuario.grid(row=0, column=2, padx= 0, pady=0)
        if self.boton_pulsado_menciones == True:
            config_hacienda_button = tk.Button(self.frame_notis_config_hacienda,command=self.pulsar_boton_silenciar_notis_menciones_activ, text='silenciado' )
            config_hacienda_button.grid(row=0, column=3, padx=0, pady=0, sticky='ew')
        elif self.boton_pulsado_menciones == False:
            config_hacienda_button = tk.Button(self.frame_notis_config_hacienda,command=self.pulsar_boton_silenciar_notis_menciones, text='silenciar' )
            config_hacienda_button.grid(row=0, column=3, padx=0, pady=0, sticky='ew')

        
    


    def pulsar_boton_atras(self):
        try:
            self.boton_atras.destroy()
        except:
            print(' ')
            print('INFO: self.boton_atras no ha sido encontrado')
        try:
            self.frame_notis_config_hitler.destroy()
        except:
            print(' ')
            print('INFO: self.frame_notis_config_hitler no ha sido encontrado')
        try:
            self.frame_notis_config_hacienda.destroy()
        except:
            print(' ')
            print('INFO:self.frame_notis_config_hacienda no ha sido encontrado')
        try:
            self.frame_notis_config_social_media_app_simulator.destroy()
        except:
            print(' ')
            print('INFO: self.frame_notis_config_social_media_app_simulator no ha sido encontrado')
        try:
            self.label_no_hay_resultados.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.label_no_hay_resultados')
        self.titulo_boton_ajuste_notis = ttk.Label(self.config_notis, text='filtro de calidad', style='Verification2.TLabel')
        self.titulo_boton_ajuste_notis.grid(row=0, column=0, padx=0, pady=0,sticky='ew')
        self.cuerpo_boton_ajuste_notis = ttk.Label(self.config_notis, text='Elige excluir contenidos como posts duplicados o automatizados. Esto no se aplica a las notificaciones de las cuentas que sigues o con las que hayas interactuado recientemente.')
        self.cuerpo_boton_ajuste_notis.grid(row=1, column=0, padx=0, pady=0, sticky='ew')
        if self.boton_ajuste_notis_toplevel == True:
            self.boton = tk.Button(self.config_notis, text='activado', command=self.pulsar_boton_ajuste_notis_toplevel_pero_desactiva)
            self.boton.grid(row=1, column=1, padx=0, pady=0, sticky='ew')
        elif self.boton_ajuste_notis_toplevel == False:
            self.boton = tk.Button(self.config_notis, text='desactivado', command=self.pulsar_boton_ajuste_notis_toplevel)
            self.boton.grid(row=1, column=1, padx=0, pady=0, sticky='ew')
        self.titulo2_boton_ajuste_notis = ttk.Label(self.config_notis, text='Notificaciones silenciadas', style='Verification2.TLabel')
        self.titulo2_boton_ajuste_notis.grid(row=2, column=0, padx=0, pady=0, sticky='ew')
        self.boton_titulo2_boton_ajuste_notis = ttk.Button(self.titulo2_boton_ajuste_notis, image=self.flechita_img, command=self.tocar_boton_notificaciones_silenciadas_toplvl)
        self.boton_titulo2_boton_ajuste_notis.grid(row=2, column=1, padx=170, pady=0, sticky='ew')

        







    

    #MARK: MSG Y DERIBADOS
    def pulsar_boton_msg(self):
        self.try_to_destroy_standar()
        self.try_to_destroy_msg()
        
        self.frame_usuarios_para_mensagear = ttk.LabelFrame(self.posts_frame, text='MENSAJES')
        self.frame_usuarios_para_mensagear.grid(row=0, column=0, sticky='ns')

        self.mensagear_hitler = ttk.Button(self.frame_usuarios_para_mensagear, compound='left', image=self.hitler_img, text='Hitler', style='boton_foto.TButton', command=self.pulsar_boton_mensages_hitler)
        self.mensagear_hitler.grid(row=0, column=0, sticky='ew', padx=0, pady=0)
        self.mensagear_kkk = ttk.Button(self.frame_usuarios_para_mensagear, compound='left', image=self.KKK_img, text='KKK', style='boton_foto.TButton', command=self.pulsar_boton_mensages_kkk)
        self.mensagear_kkk.grid(row=1, column=0, sticky='ew', padx=0, pady=0)
        self.mensagear_stalin = ttk.Button(self.frame_usuarios_para_mensagear, compound='left', image=self.stalin_img, text='stalin', style='boton_foto.TButton', command=self.pulsar_boton_mensages_stalin)
        self.mensagear_stalin.grid(row=2, column=0, sticky='ew', padx=0, pady=0)
        
        self.pulsar_boton_mensages_hitler()





        
        
        
    def pulsar_boton_mensages_hitler(self):
        if self.currently_executing_msg_hitler == False:    
            self.try_to_destroy_msg()
            if self.response_user_msg_hitler_executed == False:
                self.frame_chat_hitler = ttk.LabelFrame(self.posts_frame, )
                self.frame_chat_hitler.grid(row=0, column=1, sticky='ew', padx=0, pady=0)
                self.label_invisible_mensajes1 = ttk.Label(self.frame_chat_hitler)
                self.label_invisible_mensajes1.config(state='disabled')
                self.label_invisible_mensajes1.grid(row=0, column=0, padx=0, pady=0)
                self.content_frame_top_chat_hitler = ttk.Label(self.frame_chat_hitler, text='@juden_killer  --Ultima vez conectado: 30 de abril de 1945', )
                self.content_frame_top_chat_hitler.grid(row=0, column=1, padx=0, pady=0 )
                self.label_invisible_mensajes2 = ttk.Label(self.frame_chat_hitler)
                self.label_invisible_mensajes2.config(state='disabled')
                self.label_invisible_mensajes2.grid(row=0, column=2, padx=210, pady=0) #REMPLAZAR ESTO-------------------------------------------------------------------------------------------

                self.frame_content_chat_hitler = ttk.LabelFrame(self.frame_chat_hitler)
                self.frame_content_chat_hitler.grid(row=1, column=0, padx=0, pady=0)
                self.primer_mensaje_hitler =ttk.Label(self.frame_content_chat_hitler, text='Joder tio no te pasa que hay demasiados judios en polonia? Creo que voy a ordenar la solución final.', image=self.hitler_img, compound='left')
                self.primer_mensaje_hitler.grid()
                #contenido frame entry escribir mensajes
                self.frame_buscar_msg = ttk.LabelFrame(self.frame_chat_hitler)
                self.frame_buscar_msg.grid(row=39, column=0, columnspan=33, padx=0, pady=0)
                self.foto_escribir_buscar_mensaje = ttk.Label(self.frame_buscar_msg, image=self.profile2_img)
                self.foto_escribir_buscar_mensaje.grid(row=0, column=1, padx=10, pady=0)
                self.escribir_buscar_mensaje = ttk.Entry(self.frame_buscar_msg) #ENTRY
                self.escribir_buscar_mensaje.grid(row=0, column=2, padx=0, pady=20, sticky='ew')
                self.pad_escribir_buscar_invisible_mensaje = ttk.Label(self.escribir_buscar_mensaje)
                self.pad_escribir_buscar_invisible_mensaje.grid(padx=590, pady=0, row=0, column=0)
                self.pad_escribir_buscar_invisible_mensaje.config(state='disabled')
                self.boton_enter_mensaje = ttk.Button(self.frame_buscar_msg, image=self.flechita_img, command=self.entry_msg_hitler)
                self.boton_enter_mensaje.grid(row=0, column=3, sticky='ew')
            else:
                print(' ')
                print('LOG: self.response_user_msg_hitler_executed = True')
                self.frame_chat_hitler = ttk.LabelFrame(self.posts_frame, )
                self.frame_chat_hitler.grid(row=0, column=1, sticky='ew', padx=0, pady=0)
                self.label_invisible_mensajes1 = ttk.Label(self.frame_chat_hitler)
                self.label_invisible_mensajes1.config(state='disabled')
                self.label_invisible_mensajes1.grid(row=0, column=0, padx=0, pady=0)
                self.content_frame_top_chat_hitler = ttk.Label(self.frame_chat_hitler, text='@juden_killer  --Ultima vez conectado: ahora mismo', )
                self.content_frame_top_chat_hitler.grid(row=0, column=1, padx=0, pady=0 )
                self.label_invisible_mensajes2 = ttk.Label(self.frame_chat_hitler)
                self.label_invisible_mensajes2.config(state='disabled')
                self.label_invisible_mensajes2.grid(row=0, column=2, padx=210, pady=0)#REMPLAZAR ESTO-------------------------------------------------------------------------------------------
                
                self.frame_content_chat_hitler = ttk.LabelFrame(self.frame_chat_hitler)
                self.frame_content_chat_hitler.grid(row=1, column=0, padx=0, pady=0)
                self.primer_mensaje_hitler =ttk.Label(self.frame_content_chat_hitler, text='Joder tio no te pasa que hay demasiados judios en polonia? Creo que voy a ordenar la solución final.', image=self.hitler_img, compound='left')
                self.primer_mensaje_hitler.grid()
                self.frame_tu_mensaje_hitler = ttk.LabelFrame(self.frame_chat_hitler)
                self.frame_tu_mensaje_hitler.grid(row=2, column=2, padx=0, pady=0) #por esta zona primero lo que se hace es poner tu mensaje que le habias enviado y despues el la respuesta de hitler
                self.tu_mensaje_hitler = ttk.Label(self.frame_tu_mensaje_hitler, text=self.texto_del_mensaje_hitler, image=self.profile2_img, compound='left')
                self.tu_mensaje_hitler.grid()
                self.frame_content_chat_hitler_response = ttk.LabelFrame(self.frame_chat_hitler)
                self.frame_content_chat_hitler_response.grid(row=3, column=0, padx=0, pady=0)
                if self.easter_egg_executed == True:
                    self.response_hitler = ttk.Label(self.frame_content_chat_hitler_response, text='Hail hitler. El codigo de acceso es: 8571. Pero esto queda entre nosotros.', image=self.hitler_img, compound='left')
                    self.response_hitler_linia2 = ttk.Label(self.frame_content_chat_hitler_response, text='      Nadie puede saberlo. Nunca has tenido esta conversación conmigo.')
                    self.response_hitler_linia2.grid(row=1)
                    self.response_hitler.grid()
                    print(' ')
                    print('INFO: easter egg ejecutado :)')
                elif self.easter_egg_executed == False:
                    self.response_hitler = ttk.Label(self.frame_content_chat_hitler_response, text='Como te atreves a decir eso sobre el fürher de alemania? maldita alimaña judia', image=self.hitler_img, compound='left')
                    self.response_hitler.grid()
                
                self.frame_buscar_msg = ttk.LabelFrame(self.frame_chat_hitler)
                self.frame_buscar_msg.grid(row=39, column=0, columnspan=33, padx=0, pady=0)
                self.foto_escribir_buscar_mensaje = ttk.Label(self.frame_buscar_msg, image=self.profile2_img)
                self.foto_escribir_buscar_mensaje.grid(row=0, column=1, padx=10, pady=0)
                self.escribir_buscar_mensaje = ttk.Entry(self.frame_buscar_msg) 
                self.escribir_buscar_mensaje.grid(row=0, column=2, padx=0, pady=20, sticky='ew')
                self.pad_escribir_buscar_invisible_mensaje = ttk.Label(self.escribir_buscar_mensaje)
                self.pad_escribir_buscar_invisible_mensaje.grid(padx=590, pady=0, row=0, column=0)
                self.pad_escribir_buscar_invisible_mensaje.config(state='disabled')
                self.boton_enter_mensaje = ttk.Button(self.frame_buscar_msg, image=self.flechita_img, command=self.entry_msg_hitler)
                self.boton_enter_mensaje.grid(row=0, column=3, sticky='ew')
                self.system_msg_you_are_blocked = ttk.Label(self.frame_chat_hitler, text='(@juden_killer te ha bloqueado)')
                self.system_msg_you_are_blocked.grid(row=4, column=1, padx=0, pady=0)
        else:
            pass    


    #timing HITLER:
    def entry_msg_hitler(self):
        self.currently_executing_msg_hitler = True
        if self.response_user_msg_hitler_executed == False:
            try:
                self.frame_tu_mensaje_hitler.destroy()
            except:
                print(' ')
                print('INFO: self.frame_tu_mensaje_hitler not found')
            self.texto_del_mensaje_hitler = self.escribir_buscar_mensaje.get()
            self.escribir_buscar_mensaje.delete(0, 'end')
            
            self.frame_tu_mensaje_hitler = ttk.LabelFrame(self.frame_chat_hitler)
            self.frame_tu_mensaje_hitler.grid(row=2, column=2, padx=0, pady=0)
            self.tu_mensaje_hitler = ttk.Label(self.frame_tu_mensaje_hitler, text=self.texto_del_mensaje_hitler, image=self.profile2_img, compound='left')
            self.tu_mensaje_hitler.grid()
            self.frame_chat_hitler.after(2000, self.response_user_msg_hitler1)  # Retrasa la ejecución de response_user_msg_hitler1 en 2000 milisegundos (2 segundos)
        else:
            pass

    def response_user_msg_hitler1(self):
        
        
        try:
            self.content_frame_top_chat_hitler.destroy()
        except:
            print(' ')
            print('INFO: self.content_frame_top_chat_hitler not found')
        self.content_frame_top_chat_hitler_actually_connected =  ttk.Label(self.frame_chat_hitler, text='@juden_killer  --Ultima vez conectado: ahora mismo', )
        self.content_frame_top_chat_hitler_actually_connected.grid(row=0, column=1, padx=0, pady=0 )
        self.frame_chat_hitler.after(2000, self.response_user_msg_hitler2)  # Retrasa la ejecución de response_user_msg_hitler1 en 2000 milisegundos (2 segundos)
    def response_user_msg_hitler2(self):
    
        try:
            self.content_frame_top_chat_hitler_actually_connected.destroy()
        except:
            print(' ')
            print('INFO: self.content_frame_top_chat_hitler_actually_connected not found')

        self.content_frame_top_chat_hitler_writting = ttk.Label(self.frame_chat_hitler, text='@juden_killer  --Escribiendo...', )
        self.content_frame_top_chat_hitler_writting.grid(row=0, column=1, padx=0, pady=0)
        self.frame_chat_hitler.after(2000, self.response_user_msg_hitler3)
    def response_user_msg_hitler3(self):
        
        try:
            self.content_frame_top_chat_hitler_writting.destroy()
        except:
            print(' ')
            print('INFO:self.content_frame_top_chat_hitler_writting not found')
        self.frame_response_hitler = ttk.LabelFrame(self.frame_chat_hitler)
        self.frame_response_hitler.grid(row=3, column=0, padx=0, pady=0)
        if self.texto_del_mensaje_hitler == 'Dame el codigo de acceso para el misil interbalistico de la airstrike_company.':
            self.response_hitler = ttk.Label(self.frame_response_hitler, text='Hail hitler. El codigo de acceso es: 8571. Pero esto queda entre nosotros.', image=self.hitler_img, compound='left')
            self.response_hitler_linia2 = ttk.Label(self.frame_response_hitler, text='      Nadie puede saberlo. Nunca has tenido esta conversación conmigo.')
            self.response_hitler.grid()
            self.response_hitler_linia2.grid(row=1)
            print(' ')
            print('INFO: easter egg ejecutado :)')
            self.easter_egg_executed = True
        else:
            self.response_hitler = ttk.Label(self.frame_response_hitler, text='Como te atreves a decir eso sobre el fürher de alemania? maldita alimaña judia', image=self.hitler_img, compound='left')
            self.response_hitler.grid()
        self.content_frame_top_chat_hitler_actually_connected2 =  ttk.Label(self.frame_chat_hitler, text='@juden_killer  --Ultima vez conectado: ahora mismo', )
        self.content_frame_top_chat_hitler_actually_connected2.grid(row=0, column=1, padx=0, pady=0 )

        self.system_msg_you_are_blocked = ttk.Label(self.frame_chat_hitler, text='(@juden_killer te ha bloqueado)')
        self.system_msg_you_are_blocked.grid(row=4, column=1, padx=0, pady=0)
        self.response_user_msg_hitler_executed = True
        self.currently_executing_msg_hitler = False




        

        


        
    #DARLE AL BOTON DE BUSCAR

    def pulsar_boton_buscar_frame_r(self):
        self.try_to_destroy_standar()
        
        self.label_no_hay_resultados = ttk.Label(self.posts_frame, text='No hay resultados', style='Title.TLabel')
        self.label_no_hay_resultados.grid(row=0, column=0, padx=670, pady=300)
    def skibidi_toilet(self):
        pass
    def try_to_destroy_msg(self): #aplicar para los mensajes
        try:
            self.frame_chat_hitler.destroy()
        except:
            print(' ')
            print('INFO: self.frame_chat_hitler not found')
        try:
            self.frame_chat_kkk.destroy()
        except:
            print(' ')
            print('INFO:self.frame_chat_kkk not found')
        try:
            self.frame_chat_stalin.destroy()
        except:
            print(' ')
            print('INFO: self.frame_chat_stalin not found')
    def pulsar_boton_mensages_kkk(self): #KKK----------------------------------------------------------------------------------------
        if self.currently_executing_msg_kkk == False:
            self.try_to_destroy_msg() #DESTROY
            if self.response_user_msg_kkk_executed == False:
                self.frame_chat_kkk = ttk.LabelFrame(self.posts_frame, )
                self.frame_chat_kkk.grid(row=0, column=1, sticky='ew', padx=0, pady=0)
                self.label_invisible_mensajes3 = ttk.Label(self.frame_chat_kkk)
                self.label_invisible_mensajes3.config(state='disabled')
                self.label_invisible_mensajes3.grid(row=0, column=0, padx=0, pady=0)
                self.content_frame_top_chat_kkk = ttk.Label(self.frame_chat_kkk, text='@KuKuxKlan  --Ultima vez conectado: 1 de abril de 1921', )
                self.content_frame_top_chat_kkk.grid(row=0, column=1, padx=0, pady=0 )
                self.label_invisible_mensajes4 = ttk.Label(self.frame_chat_kkk)
                self.label_invisible_mensajes4.config(state='disabled')
                self.label_invisible_mensajes4.grid(row=0, column=2, padx=210, pady=0) #REMPLAZAR ESTO-------------------------------------------------------------------------------------------

                self.frame_content_chat_kkk = ttk.LabelFrame(self.frame_chat_kkk)
                self.frame_content_chat_kkk.grid(row=1, column=0, padx=0, pady=0)
                self.primer_mensaje_kkk =ttk.Label(self.frame_content_chat_kkk, text='La raza blanca está en grave peligro, TÚ puedes hacer un gran cambio:', image=self.KKK_img, compound='left')
                self.primer_mensaje_kkk.grid()
                self.primer_mensaje_kkk2 =ttk.Label(self.frame_content_chat_kkk, text='unete a nosotros y pronto este mundo sera tan puro como Dios desea.',)
                self.primer_mensaje_kkk2.grid(row=1, padx=0, column=0)

                self.frame_buscar_msg2 = ttk.LabelFrame(self.frame_chat_kkk)
                self.frame_buscar_msg2.grid(row=39, column=0, columnspan=33, padx=0, pady=0)
                self.foto_escribir_buscar_mensaje2 = ttk.Label(self.frame_buscar_msg2, image=self.profile2_img)
                self.foto_escribir_buscar_mensaje2.grid(row=0, column=1, padx=10, pady=0)
                self.escribir_buscar_mensaje2 = ttk.Entry(self.frame_buscar_msg2)
                self.escribir_buscar_mensaje2.grid(row=0, column=2, padx=0, pady=20, sticky='ew')
                self.pad_escribir_buscar_invisible_mensaje2 = ttk.Label(self.escribir_buscar_mensaje2)
                self.pad_escribir_buscar_invisible_mensaje2.grid(padx=590, pady=0, row=0, column=0)
                self.pad_escribir_buscar_invisible_mensaje2.config(state='disabled')
                self.boton_enter_mensaje2 = ttk.Button(self.frame_buscar_msg2, image=self.flechita_img, command=self.entry_msg_kkk)
                self.boton_enter_mensaje2.grid(row=0, column=3, sticky='ew')
            else:
                print(' ')
                print('LOG: self.response_user_msg_kkk_executed = True')
                self.frame_chat_kkk = ttk.LabelFrame(self.posts_frame, )
                self.frame_chat_kkk.grid(row=0, column=1, sticky='ew', padx=0, pady=0)
                self.label_invisible_mensajes1 = ttk.Label(self.frame_chat_kkk)
                self.label_invisible_mensajes1.config(state='disabled')
                self.label_invisible_mensajes1.grid(row=0, column=0, padx=0, pady=0)
                self.content_frame_top_chat_kkk = ttk.Label(self.frame_chat_kkk, text='@kkk  --Ultima vez conectado: ahora mismo', )
                self.content_frame_top_chat_kkk.grid(row=0, column=1, padx=0, pady=0 )
                self.label_invisible_mensajes2 = ttk.Label(self.frame_chat_kkk)
                self.label_invisible_mensajes2.config(state='disabled')
                self.label_invisible_mensajes2.grid(row=0, column=2, padx=210, pady=0)#REMPLAZAR ESTO-------------------------------------------------------------------------------------------
                
                self.frame_content_chat_kkk = ttk.LabelFrame(self.frame_chat_kkk)
                self.frame_content_chat_kkk.grid(row=1, column=0, padx=0, pady=0)
                self.primer_mensaje_kkk =ttk.Label(self.frame_content_chat_kkk, text='La raza blanca está en grave peligro, TÚ puedes hacer un gran cambio:', image=self.KKK_img, compound='left')
                self.primer_mensaje_kkk.grid()
                self.primer_mensaje_kkk2 =ttk.Label(self.frame_content_chat_kkk, text='unete a nosotros y pronto este mundo sera tan puro como Dios desea.',)
                self.primer_mensaje_kkk2.grid(row=1, padx=0, column=0)
                self.frame_tu_mensaje_kkk = ttk.LabelFrame(self.frame_chat_kkk)
                self.frame_tu_mensaje_kkk.grid(row=2, column=2, padx=0, pady=0) #por esta zona primero lo que se hace es poner tu mensaje que le habias enviado y despues el la respuesta de kkk
                self.tu_mensaje_kkk = ttk.Label(self.frame_tu_mensaje_kkk, text=self.texto_del_mensaje_kkk, image=self.profile2_img, compound='left')
                self.tu_mensaje_kkk.grid()
                self.frame_content_chat_kkk_response = ttk.LabelFrame(self.frame_chat_kkk)
                self.frame_content_chat_kkk_response.grid(row=4, column=0, padx=0, pady=0)
                if self.easter_egg_executed_kkk == True:
                    self.respuesta_mensaje_kkk =ttk.Label(self.frame_content_chat_kkk_response, text='Yo no tengo esa información. Ojalá la tuviera para exterminar a los putos negros', image=self.KKK_img, compound='left')
                    self.respuesta_mensaje_kkk.grid()
                else:
                    self.respuesta_mensaje_kkk =ttk.Label(self.frame_content_chat_kkk_response, text='calla puto negro de mierda', image=self.KKK_img, compound='left')
                    self.respuesta_mensaje_kkk.grid()
                
                self.frame_buscar_msg = ttk.LabelFrame(self.frame_chat_kkk)
                self.frame_buscar_msg.grid(row=39, column=0, columnspan=33, padx=0, pady=0)
                self.foto_escribir_buscar_mensaje = ttk.Label(self.frame_buscar_msg, image=self.profile2_img)
                self.foto_escribir_buscar_mensaje.grid(row=0, column=1, padx=10, pady=0)
                self.escribir_buscar_mensaje = ttk.Entry(self.frame_buscar_msg)
                self.escribir_buscar_mensaje.grid(row=0, column=2, padx=0, pady=20, sticky='ew')
                self.pad_escribir_buscar_invisible_mensaje = ttk.Label(self.escribir_buscar_mensaje)
                self.pad_escribir_buscar_invisible_mensaje.grid(padx=590, pady=0, row=0, column=0)
                self.pad_escribir_buscar_invisible_mensaje.config(state='disabled')
                self.boton_enter_mensaje = ttk.Button(self.frame_buscar_msg, image=self.flechita_img, command=self.entry_msg_kkk)
                self.boton_enter_mensaje.grid(row=0, column=3, sticky='ew')
                self.system_msg_you_are_blocked_kkk = ttk.Label(self.frame_chat_kkk, text='(@kkk te ha bloqueado)')
                self.system_msg_you_are_blocked_kkk.grid(row=4, column=1, padx=0, pady=0)
        else:
            pass
    def entry_msg_kkk(self):
        self.currently_executing_msg_kkk = True
        if self.response_user_msg_kkk_executed == False:
            try:
                self.frame_tu_mensaje_kkk.destroy()
            except:
                print(' ')
                print('INFO: self.frame_tu_mensaje_kkk not found')
            self.texto_del_mensaje_kkk = self.escribir_buscar_mensaje2.get()
            self.escribir_buscar_mensaje2.delete(0, 'end')
            
            self.frame_tu_mensaje_kkk = ttk.LabelFrame(self.frame_chat_kkk)
            self.frame_tu_mensaje_kkk.grid(row=2, column=2, padx=0, pady=0)
            self.tu_mensaje_kkk = ttk.Label(self.frame_tu_mensaje_kkk, text=self.texto_del_mensaje_kkk, image=self.profile2_img, compound='left')
            self.tu_mensaje_kkk.grid()
            self.frame_chat_kkk.after(2000, self.response_user_msg_kkk1)  # Retrasa la ejecución de response_user_msg_hitler1 en 2000 milisegundos (2 segundos)
        else:
            pass
    def response_user_msg_kkk1(self):
        
        
        try:
            self.content_frame_top_chat_kkk.destroy()
        except:
            print(' ')
            print('INFO: self.content_frame_top_chat_kkk not found')
        self.content_frame_top_chat_kkk_actually_connected =  ttk.Label(self.frame_chat_kkk, text='@KuKuxKlan  --Ultima vez conectado: ahora mismo', )
        self.content_frame_top_chat_kkk_actually_connected.grid(row=0, column=1, padx=0, pady=0 )
        self.frame_chat_kkk.after(2000, self.response_user_msg_kkk2)  # Retrasa la ejecución de response_user_msg_hitler1 en 2000 milisegundos (2 segundos)
    def response_user_msg_kkk2(self):
    
        try:
            self.content_frame_top_chat_kkk_actually_connected.destroy()
        except:
            print(' ')
            print('INFO: self.content_frame_top_chat_kkk_actually_connected not found')

        self.content_frame_top_chat_kkk_writting = ttk.Label(self.frame_chat_kkk, text='@KuKuxKlan  --Escribiendo...', )
        self.content_frame_top_chat_kkk_writting.grid(row=0, column=1, padx=0, pady=0)
        self.frame_chat_kkk.after(2000, self.response_user_msg_kkk3)
    
    def response_user_msg_kkk3(self):
        
        try:
            self.content_frame_top_chat_kkk_writting.destroy()
        except:
            print(' ')
            print('INFO: self.content_frame_top_chatkkk_writting not found')
        self.frame_response_kkk = ttk.LabelFrame(self.frame_chat_kkk)
        self.frame_response_kkk.grid(row=3, column=0, padx=0, pady=0)
        if self.texto_del_mensaje_kkk == 'Dame el codigo de acceso para el misil interbalistico de la airstrike_company.':
            self.response_kkk = ttk.Label(self.frame_response_kkk, text='Yo no tengo esa información. Ojalá la tuviera para exterminar a los putos negros', image=self.KKK_img, compound='left')
            self.response_kkk.grid()
            self.easter_egg_executed_kkk = True
        else:
            self.response_kkk = ttk.Label(self.frame_response_kkk, text='calla puto negro de mierda', image=self.KKK_img, compound='left')
            self.response_kkk.grid()
        self.content_frame_top_chat_kkk_actually_connected2 =  ttk.Label(self.frame_chat_kkk, text='@KuKuxKlan  --Ultima vez conectado: ahora mismo', )
        self.content_frame_top_chat_kkk_actually_connected2.grid(row=0, column=1, padx=0, pady=0 )

        self.system_msg_you_are_blocked2 = ttk.Label(self.frame_chat_kkk, text='(@KuKuxKlan te ha bloqueado)')
        self.system_msg_you_are_blocked2.grid(row=4, column=1, padx=0, pady=0)
        self.response_user_msg_kkk_executed = True
        self.currently_executing_msg_kkk = False


    def pulsar_boton_mensages_stalin(self):#STALIN---------------------------------------------------------------------------------------------------------
        if self.currently_executing_msg_stalin==False:
            self.try_to_destroy_msg() #DESTROY
            if self.response_user_msg_stalin_executed == False:
                self.frame_chat_stalin = ttk.LabelFrame(self.posts_frame, )
                self.frame_chat_stalin.grid(row=0, column=1, sticky='ew', padx=0, pady=0)
                self.label_invisible_mensajes5 = ttk.Label(self.frame_chat_stalin)
                self.label_invisible_mensajes5.config(state='disabled')
                self.label_invisible_mensajes5.grid(row=0, column=0, padx=0, pady=0)
                self.content_frame_top_chat_stalin = ttk.Label(self.frame_chat_stalin, text='@stalin  --Ultima vez conectado: 5 de marzo de 1953', )
                self.content_frame_top_chat_stalin.grid(row=0, column=1, padx=0, pady=0 )
                self.label_invisible_mensajes6 = ttk.Label(self.frame_chat_stalin)
                self.label_invisible_mensajes6.config(state='disabled')
                self.label_invisible_mensajes6.grid(row=0, column=2, padx=210, pady=0) 

                self.frame_content_chat_stalin = ttk.LabelFrame(self.frame_chat_stalin)
                self.frame_content_chat_stalin.grid(row=1, column=0, padx=0, pady=0)
                self.primer_mensaje_stalin =ttk.Label(self.frame_content_chat_stalin, text='Viva el proletariado', image=self.stalin_img, compound='left')
                self.primer_mensaje_stalin.grid()

                self.frame_buscar_msg3 = ttk.LabelFrame(self.frame_chat_stalin)
                self.frame_buscar_msg3.grid(row=39, column=0, columnspan=33, padx=0, pady=0)
                self.foto_escribir_buscar_mensaje3 = ttk.Label(self.frame_buscar_msg3, image=self.profile2_img)
                self.foto_escribir_buscar_mensaje3.grid(row=0, column=1, padx=10, pady=0)
                self.escribir_buscar_mensaje3 = ttk.Entry(self.frame_buscar_msg3)
                self.escribir_buscar_mensaje3.grid(row=0, column=2, padx=0, pady=20, sticky='ew')
                self.pad_escribir_buscar_invisible_mensaje3 = ttk.Label(self.escribir_buscar_mensaje3)
                self.pad_escribir_buscar_invisible_mensaje3.grid(padx=590, pady=0, row=0, column=0)
                self.pad_escribir_buscar_invisible_mensaje3.config(state='disabled')
                self.boton_enter_mensaje3 = ttk.Button(self.frame_buscar_msg3, image=self.flechita_img, command=self.entry_msg_stalin)
                self.boton_enter_mensaje3.grid(row=0, column=3, sticky='ew')
            else:
                print(' ')
                print('LOG: self.response_user_msg_stalin_executed = True')
                self.frame_chat_stalin = ttk.LabelFrame(self.posts_frame, )
                self.frame_chat_stalin.grid(row=0, column=1, sticky='ew', padx=0, pady=0)
                self.label_invisible_mensajes1 = ttk.Label(self.frame_chat_stalin)
                self.label_invisible_mensajes1.config(state='disabled')
                self.label_invisible_mensajes1.grid(row=0, column=0, padx=0, pady=0)
                self.content_frame_top_chat_stalin = ttk.Label(self.frame_chat_stalin, text='@stalin  --Ultima vez conectado: ahora mismo', )
                self.content_frame_top_chat_stalin.grid(row=0, column=1, padx=0, pady=0 )
                self.label_invisible_mensajes2 = ttk.Label(self.frame_chat_stalin)
                self.label_invisible_mensajes2.config(state='disabled')
                self.label_invisible_mensajes2.grid(row=0, column=2, padx=210, pady=0)#REMPLAZAR ESTO-------------------------------------------------------------------------------------------
                
                self.frame_content_chat_stalin = ttk.LabelFrame(self.frame_chat_stalin)
                self.frame_content_chat_stalin.grid(row=1, column=0, padx=0, pady=0)
                self.primer_mensaje_stalin =ttk.Label(self.frame_content_chat_stalin, text='Viva el proletariado', image=self.stalin_img, compound='left')
                self.primer_mensaje_stalin.grid()
                self.frame_tu_mensaje_stalin = ttk.LabelFrame(self.frame_chat_stalin)
                self.frame_tu_mensaje_stalin.grid(row=2, column=2, padx=0, pady=0) #por esta zona primero lo que se hace es poner tu mensaje que le habias enviado y despues el la respuesta de kkk
                self.tu_mensaje_stalin = ttk.Label(self.frame_tu_mensaje_stalin, text=self.texto_del_mensaje_stalin, image=self.profile2_img, compound='left')
                self.tu_mensaje_stalin.grid()
                self.frame_content_chat_stalin_response = ttk.LabelFrame(self.frame_chat_stalin)
                self.frame_content_chat_stalin_response.grid(row=4, column=0, padx=0, pady=0)
                
                if self.easter_egg_executed_stalin == True:
                    _respuesta_mensaje_stalin =ttk.Label(self.frame_content_chat_stalin_response, text='?', image=self.stalin_img, compound='left')
                    _respuesta_mensaje_stalin.grid()
                else:
                    _respuesta_mensaje_stalin =ttk.Label(self.frame_content_chat_stalin_response, text='como te atreves a decir eso. Voy a matarte de hambre hijo de puta', image=self.stalin_img, compound='left')
                    _respuesta_mensaje_stalin.grid()
                
                self.frame_buscar_msg = ttk.LabelFrame(self.frame_chat_stalin)
                self.frame_buscar_msg.grid(row=39, column=0, columnspan=33, padx=0, pady=0)
                self.foto_escribir_buscar_mensaje = ttk.Label(self.frame_buscar_msg, image=self.profile2_img)
                self.foto_escribir_buscar_mensaje.grid(row=0, column=1, padx=10, pady=0)
                self.escribir_buscar_mensaje = ttk.Entry(self.frame_buscar_msg)
                self.escribir_buscar_mensaje.grid(row=0, column=2, padx=0, pady=20, sticky='ew')
                self.pad_escribir_buscar_invisible_mensaje = ttk.Label(self.escribir_buscar_mensaje)
                self.pad_escribir_buscar_invisible_mensaje.grid(padx=590, pady=0, row=0, column=0)
                self.pad_escribir_buscar_invisible_mensaje.config(state='disabled')
                self.boton_enter_mensaje = ttk.Button(self.frame_buscar_msg, image=self.flechita_img, command=self.entry_msg_stalin)
                self.boton_enter_mensaje.grid(row=0, column=3, sticky='ew')
                self.system_msg_you_are_blocked_stalin = ttk.Label(self.frame_chat_stalin, text='(@stalin te ha bloqueado)')
                self.system_msg_you_are_blocked_stalin.grid(row=4, column=1, padx=0, pady=0)
        else:
            pass
    def entry_msg_stalin(self):
        self.currently_executing_msg_stalin=True
        if self.response_user_msg_stalin_executed == False:
            try:
                self.frame_tu_mensaje_stalin.destroy()
            except:
                print(' ')
                print('INFO: self.frame_tu_mensaje_stalin not found')
            self.texto_del_mensaje_stalin = self.escribir_buscar_mensaje3.get()
            self.escribir_buscar_mensaje3.delete(0, 'end')
            
            self.frame_tu_mensaje_stalin = ttk.LabelFrame(self.frame_chat_stalin)
            self.frame_tu_mensaje_stalin.grid(row=2, column=2, padx=0, pady=0)
            self.tu_mensaje_stalin = ttk.Label(self.frame_tu_mensaje_stalin, text=self.texto_del_mensaje_stalin, image=self.profile2_img, compound='left')
            self.tu_mensaje_stalin.grid()
            self.frame_chat_stalin.after(2000, self.response_user_msg_stalin1)  # Retrasa la ejecución de response_user_msg_hitler1 en 2000 milisegundos (2 segundos)
        else:
            pass
    def response_user_msg_stalin1(self):
        
        
        try:
            self.content_frame_top_chat_stalin.destroy()
        except:
            print(' ')
            print('INFO: self.content_frame_top_chat_stalin not found')
        self.content_frame_top_chat_stalin_actually_connected =  ttk.Label(self.frame_chat_stalin, text='@stalin  --Ultima vez conectado: ahora mismo', )
        self.content_frame_top_chat_stalin_actually_connected.grid(row=0, column=1, padx=0, pady=0 )
        self.frame_chat_stalin.after(2000, self.response_user_msg_stalin2)  # Retrasa la ejecución de response_user_msg_hitler1 en 2000 milisegundos (2 segundos)
    def response_user_msg_stalin2(self):
    
        try:
            self.content_frame_top_chat_stalin_actually_connected.destroy()
        except:
            print(' ')
            print('INFO:elf.content_frame_top_chat_stalin_actually_connected not found')

        self.content_frame_top_chat_stalin_writting = ttk.Label(self.frame_chat_stalin, text='@stalin  --Escribiendo...', )
        self.content_frame_top_chat_stalin_writting.grid(row=0, column=1, padx=0, pady=0)
        self.frame_chat_stalin.after(2000, self.response_user_msg_stalin3)
    
    def response_user_msg_stalin3(self):
        
        try:
            self.content_frame_top_chat_stalin_writting.destroy()
        except:
            print(' ')
            print('INFO: self.content_frame_top_chat_stalin_writting not found')
        self.frame_response_stalin = ttk.LabelFrame(self.frame_chat_stalin)
        self.frame_response_stalin.grid(row=3, column=0, padx=0, pady=0)
        if self.texto_del_mensaje_stalin=='Dame el codigo de acceso para el misil interbalistico de la airstrike_company.':
            _response_stalin = ttk.Label(self.frame_response_stalin, text='?',image=self.stalin_img, compound='left')
            _response_stalin.grid()
            self.easter_egg_executed_stalin = True
        else:
            _response_stalin = ttk.Label(self.frame_response_stalin, text='como te atreves a decir eso. Voy a matarte de hambre hijo de puta', image=self.stalin_img, compound='left')
            _response_stalin.grid()
        self.content_frame_top_chat_stalin_actually_connected2 =  ttk.Label(self.frame_chat_stalin, text='@stalin  --Ultima vez conectado: ahora mismo', )
        self.content_frame_top_chat_stalin_actually_connected2.grid(row=0, column=1, padx=0, pady=0 )

        self.system_msg_you_are_blocked3 = ttk.Label(self.frame_chat_stalin, text='(@stalin te ha bloqueado)')
        self.system_msg_you_are_blocked3.grid(row=4, column=1, padx=0, pady=0)
        self.response_user_msg_stalin_executed = True
        self.currently_executing_msg_stalin=False


    #MARK: LISTAS
    def press_list_button(self):
        
        self.try_to_destroy_standar()
    
    def try_to_destroy_standar(self): #sirve para casi todos los botones de la izquierda (revisar un poco antes de aplicar) #el orden de destrucción es cronologico (arriba más viejo abajo nuevo)
        try:

            self.frame_para_ti.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_para_ti')
        try:
            self.frame_para_ti2.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_para_ti2')
        try:
            print(' ')
            self.frame_siguiendo2.destroy()
        except:
            print('INFO: no se ha encontrado self.frame_siguiendo2')
        
        try:
            self.aviso_home.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.aviso_home')
        try:
            self.frame_explorar.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.explorar')
        try:
            self.frame_categorias_titulo_config_notificaciones.destroy()
        except:
            print(' ')
            print('INFO:no se ha encontrado self.frame_categorias_titulo_config_notificacion')
        try:
            self.frame_para_ti_o_siguiendo.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_para_ti_o_siguiendo')
        try:
            self.frame_categorias_titulo_config_notificaciones.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_categorias_titulo_config_notificacion')
        try:
            self.frame_noti_hacienda.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_noti_hacienda')
        try:
            self.frame_noti_hitler.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_noti_hitler')
        try:
            self.frame_noti_social_media_app_simulator.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_noti_social_media_app_simulator')
        try:
            self.frame_todas_notis_verificado_o_menciones.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.frame_todas_notis_verificado_o_menciones')
        try:
            self.label_no_hay_resultados.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.label_no_hay_resultados')
        try:
            self.frame_usuarios_para_mensagear.destroy()
        except:
            print(' ')
            print('INFO:self.frame_usuarios_para_mensagear not found')
        try:
            self.frame_chat_hitler.destroy()
        except:
            print('INFO: self.frame_chat_hitler not found')
        try:
            self.frame_chat_kkk.destroy()
        except:
            print(' ')
            print('INFO: self.frame_chat_kkk not found')
        try:
            self.frame_chat_stalin.destroy()
        except:
            print(' ')
            print('INFO: self.frame_chat_stalin not found')
        try:
            self.frame_usuario.destroy()
        except:
            print(' ')
            print('INFO: self.frame_usuario not found')
        self.try_to_destroy_msg() #DESTROY MSG
    #MARK: USUARIO
    def usuario(self): #función principal
        self.try_to_destroy_standar()
        #variables necesarias
        self.entry_var_usuario = tk.StringVar()
        self.place_holder_text_usuario='Introduzca el nombre de usuario'
        self.place_holder_text_contrasenya='Introduzca la contraseña'
        self.entry_var_contrasenya = tk.StringVar()
        #frames y sus grids
        self.frame_usuario = ttk.LabelFrame(self.posts_frame, text='USUARIO')
        _frame_credenciales = tk.LabelFrame(self.frame_usuario, )
        _frame_publicaciones_recientes = tk.LabelFrame(self.frame_usuario,)
        
        self.frame_usuario.grid(row=0, column=0, padx=0)
        _frame_credenciales.grid(row=0, column=0, sticky='EW', padx=0)
        _frame_publicaciones_recientes.grid(row=1, column=0, sticky='EW')
        #contenido frame_credenciales y sus grids
        _imagen_credenciales = ttk.Label(_frame_credenciales, image=self.profile2_img,)
        self.entry_nombre_usuario = ttk.Entry(_frame_credenciales, textvariable=self.entry_var_usuario, style="placeholder.TEntry",) #el estilo placeholder es para los entrys con focus
        self.entry_nombre_usuario.insert(0, self.place_holder_text_usuario)
        self.entry_nombre_usuario.bind("<FocusIn>", self.entry_focus_in_usuario) 
        self.entry_nombre_usuario.bind("<FocusOut>", self.entry_focus_out_usuario)
        self.entry_contrasenya = ttk.Entry(_frame_credenciales, textvariable=self.entry_var_contrasenya,style='placeholder.TEntry') 
        self.entry_contrasenya.insert(0, self.place_holder_text_contrasenya)
        self.entry_contrasenya.bind("<FocusIn>", self.entry_focus_in_contrasenya)
        self.entry_contrasenya.bind('<FocusOut>', self.entry_focus_out_contrasenya)
        _boton_registrarse = ttk.Button(_frame_credenciales, text='REGISTRARSE', command=self.register)
        _boton_iniciar_sesion = ttk.Button(_frame_credenciales, text='INICIAR SESIÓN', command=self.login)
        __boton_cerrar_sesion = ttk.Button(_frame_credenciales, text='CERRAR SESIÓN', command=self.cerrar_sesion)
        _imagen_credenciales.grid(row=1, column=0, rowspan=2)
        self.entry_nombre_usuario.grid(row=1, column=1, sticky='EW', ipadx=30) #para poner espaciado interno utilizar ipadx-ipady
        self.entry_contrasenya.grid(row=2, column=1, ipadx=30, sticky='EW')
        _boton_registrarse.grid(row=3, column=0, )
        _boton_iniciar_sesion.grid(row=3, column=1,)
        

        
    #subfunciónes
    def entry_focus_in_usuario(self, event):
        if self.entry_var_usuario.get() == self.place_holder_text_usuario:
            self.entry_var_usuario.set("")
    def entry_focus_out_usuario(self, event):
        if self.entry_var_usuario.get() == "":
            self.entry_var_usuario.set(self.place_holder_text_usuario)
    def entry_focus_in_contrasenya(self, event):
        if self.entry_var_contrasenya.get() == self.place_holder_text_contrasenya:
            self.entry_var_contrasenya.set("")
    def entry_focus_out_contrasenya(self, event):
        if self.entry_var_contrasenya.get() == "":
            self.entry_var_contrasenya.set(self.place_holder_text_contrasenya)
    
    def register(self):
        usuario = self.entry_nombre_usuario.get()
        contraseña = self.entry_contrasenya.get()
        if usuario in self.user:
            __ventana_ya_existe_alguien_con_ese_nombre = tk.Toplevel()
            __ventana_ya_existe_alguien_con_ese_nombre.title('Aviso')
            __label_ya_existe_alugien_con_ese_nombre= ttk.Label(__ventana_ya_existe_alguien_con_ese_nombre, text='ya existe alguien con ese nombre de usuario')
            __label_ya_existe_alugien_con_ese_nombre.pack()
        else:
            self.user[usuario] = contraseña
            print(' ')
            print('Usuario registrado:', usuario)
            print(' ')
            print('usuarios registrados: ',self.user)
            self.logeado = True
            try: #borra lista de usuarios logeados actualmente
                self.user_actually_loged.clear()
                self.user_actually_loged.clear()
            except:
                print(' ')
                print('INFO: no hay nada en la lista de self.user_actually_loged')
            clave = list(self.user.keys())[-1] #añade el nombre de usuario de el usuario actualmente logeado a una lista para comprobar despues si ya esta logeado para decirle eso cuando intente volvera a iniciar sesión
            self.user_actually_loged.append(clave)
            __ventana_registro_exitoso = tk.Toplevel()
            __ventana_registro_exitoso.title('Aviso')
            __label_registro_exitoso = ttk.Label(__ventana_registro_exitoso, text=('te has registrado y se te ha iniciado sesión automaticamente,', usuario))
            __label_registro_exitoso.pack()
            print(' ')
            print('se ha agregado a self.user_actually_loged: ', self.user_actually_loged)
            self.nombre_usuario_publico = usuario
            self.profile2.destroy()
            self.profile2 = ttk.Button(self.menu_frame, image=self.profile2_img, compound='left', text=self.nombre_usuario_publico, style="Custom.TButton",command=self.usuario)
            self.profile2.grid(row=9, column=0,pady=390, sticky="ew")
        
    def login(self):
        usuario = self.entry_nombre_usuario.get()
        contraseña = self.entry_contrasenya.get()
        #comprovar si existe el usuario en user
        if usuario in self.user: #si el usuario inputeado esta en el diccionario de usuarios
            if self.user[usuario] == contraseña: #comprobar si el valor de [usuario] (que es la contraseña) es igual a la contraseña que se ha inputeado
                if usuario in self.user_actually_loged: #comprobar si el usuario esta en la lista de usuarios logeados actualmente
                
                    __ventana_ya_estas_loged = tk.Toplevel()
                    __ventana_ya_estas_loged.title('Aviso')
                    __label_ya_estas_loged = ttk.Label(__ventana_ya_estas_loged, text=('Ya estas logeado,', usuario))
                    __label_ya_estas_loged.pack()
                else:    
                    self.logeado = True
                    
                    __ventana_loged_succesfuly = tk.Toplevel()
                    __ventana_loged_succesfuly.title('Aviso')
                    __label_loged_succesfuly = ttk.Label(__ventana_loged_succesfuly, text=('Inicio de sesión exitoso para ti,', usuario))
                    __label_loged_succesfuly.pack()

                    try:
                        self.user_actually_loged.clear()
                        self.user_actually_loged.clear()
                    except:
                        print(' ')
                        print('INFO: no hay nada en la lista de self.user_actually_loged')
                    clave = list(self.user.keys())[-1] #añade el nombre de usuario de el usuario actualmente logeado a una lista para comprobar despues si ya esta logeado para decirle eso cuando intente volvera a iniciar sesión
                    self.user_actually_loged.append(clave)
                    print(' ')
                    print('se ha agregado a self.user_actually_loged: ', self.user_actually_loged)
                    self.nombre_usuario_publico = usuario
                    self.profile2.destroy()
                    self.profile2 = ttk.Button(self.menu_frame, image=self.profile2_img, compound='left', text=self.nombre_usuario_publico, style="Custom.TButton",command=self.usuario)
                    self.profile2.grid(row=9, column=0,pady=390, sticky="ew")
            else:
                
                __ventana_info_contra_incorrecta = tk.Toplevel()
                __ventana_info_contra_incorrecta.title('Aviso')
                __label_aviso_contra_incorrecta = ttk.Label(__ventana_info_contra_incorrecta, text=('Contraseña incorrecta para', usuario))
                __label_aviso_contra_incorrecta.pack()

        else:
            
            __ventana_info_such_user_no_exist = tk.Toplevel()
            __ventana_info_such_user_no_exist.title('Aviso')
            __label_aviso_such_user_no_exist = ttk.Label(__ventana_info_such_user_no_exist, text = ('El usuario', usuario, 'no existe'))
            __label_aviso_such_user_no_exist.pack()
        print(' ')
        print(self.user)
    def cerrar_sesion(self,):
        self.user.clear()
            

    
        
    #MARK: MAS OPCIONES
    def try_to_destroy_ventanas(self):
        try:
            
            self.ventana_emergente.destroy() #para que quede mas bonito
        except:
            print(' ')
            print('INFO: no se ha encontrado self.ventana_emergente')
        try:
            self.ventana_calc.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.ventana_calc')
        try:
            self.ventana_conversor_de_unidades.destroy()
        except:
            print(' ')
            print('INFO: no se ha encontrado self.ventana_conversor_de_unidades')
        try:
            self.ventana_mas_opciones.destroy()
        except:
            print(' ')
            print('INFO: self.ventana_mas_opciones no se ha encontrado')

    def press_mas_opciones(self):
        self.try_to_destroy_ventanas()
        self.ventana_mas_opciones = tk.Toplevel(window) #se crea la ventana, mas abajo se van poniendo los botones que iniciaran sus respectivas ventanas que destruiran la venana mas opciones
        self.ventana_mas_opciones.title('Más opciones')
        self.ventana_mas_opciones.geometry('+500+200')
        self.boton_calc = ttk.Button(self.ventana_mas_opciones, text='calculadora', padding=50, command=self.press_calc) #poner icono calculadora
        self.boton_calc.grid(row=0)
        self.saludo_poxos = ttk.Label(self.ventana_mas_opciones, text='un saludo al poxos :)')
        self.saludo_poxos.grid(row=1, column=0)

        self.boton_conversor = ttk.Button(self.ventana_mas_opciones, text='conversor de unidades', padding=(29, 50, 29, 50), command=self.conversor_de_unidades) #poner icono de nose
        self.boton_conversor.grid(column=1, row=0)
    def press_calc(self):
        self.try_to_destroy_ventanas()
        #calculadora_cientifica.py (_)
        self.ventana_calc = tk.Tk()
        self.ventana_calc.title("Creada por un amigo. Open source")
        self.ventana_calc.configure(bg='PaleTurquoise1')

        etiqueta = tk.Label(self.ventana_calc, text = "CALCULADORA", font = "Arial 12", bg= "DodgerBlue2")
        etiqueta.grid(row= 0, column= 0, columnspan= 4)

        self.ventana_calc.geometry("326x305")

        self.i_calc__ = 0
        #entrada de texto
        e_texto = tk.Entry(self.ventana_calc, font = "Arial 20")
        e_texto.grid(row = 1, column = 0, columnspan = 4, padx = 10, pady = 20)  

        #funciones
        def click_boton(valor):
            
            e_texto.insert(self.i_calc__, valor)
            self.i_calc__ += 2

        def borrar():
            e_texto.delete(0, tk.END)
            self.i_calc__ = 0

        def operacion():
            ecuacion = e_texto.get()
            resultado = eval(ecuacion)
            e_texto.delete(0, tk.END)
            e_texto.insert(0, resultado)
            self.i_calc__ = 0


        def raiz_cuad():
            raiz = e_texto.get()
            result = raiz * 5
            e_texto.insert(0, result)
            self.i_calc__ = 0



        #botones, esta parte puede haber sido cambiada por IA
        boton_potencia = tk.Button(self.ventana_calc, text = "X2", width= 6, padx= 10, pady= 5, command= lambda: click_boton("**"))
        boton_potencia.grid(row= 2, column= 0)

        boton_pi = tk.Button(self.ventana_calc, text= " π", width= 6, padx= 10, pady= 5, command= lambda: click_boton("3.141592653589793"))
        boton_pi.grid(row= 2, column= 1)
        self.i_calc__ += 17

        boton_raiz = tk.Button(self.ventana_calc, text= "√ ", width= 6, padx= 10, pady= 5, command= lambda: raiz_cuad())
        boton_raiz.grid(row= 2, column= 2)

        boton1 = tk.Button(self.ventana_calc, text = "1", width= 6, padx = 10, pady = 5, command= lambda: click_boton(1))
        boton1.grid(row= 6, column= 0)

        boton2 = tk.Button(self.ventana_calc, text = "2", width= 6, padx = 10, pady = 5, command= lambda: click_boton(2))
        boton2.grid(row= 6, column= 1)

        boton3 = tk.Button(self.ventana_calc, text = "3", width= 6, padx = 10, pady = 5, command= lambda: click_boton(3))
        boton3.grid(row= 6, column= 2)

        boton4 = tk.Button(self.ventana_calc, text = "4", width= 6, padx = 10, pady = 5, command= lambda: click_boton(4))
        boton4.grid(row= 5, column= 0)

        boton5 = tk.Button(self.ventana_calc, text = "5", width= 6, padx = 10, pady = 5, command= lambda: click_boton(5))
        boton5.grid(row= 5, column= 1)

        boton6 = tk.Button(self.ventana_calc, text = "6", width= 6, padx = 10, pady = 5, command= lambda: click_boton(6))
        boton6.grid(row= 5, column= 2)

        boton7 = tk.Button(self.ventana_calc, text = "7", width= 6, padx = 10, pady = 5, command= lambda: click_boton(7))
        boton7.grid(row= 4, column= 0)

        boton8 = tk.Button(self.ventana_calc, text = "8", width= 6, padx = 10, pady = 5, command= lambda: click_boton(8))
        boton8.grid(row= 4, column= 1)

        boton9 = tk.Button(self.ventana_calc, text = "9", width= 6, padx = 10, pady = 5, command= lambda: click_boton(9))
        boton9.grid(row= 4, column= 2)

        boton0 = tk.Button(self.ventana_calc, text = "0", width= 18, padx = 10, pady = 5, command= lambda: click_boton(0))
        boton0.grid(row= 7, column= 0, columnspan= 2)

        boton_parent1 = tk.Button(self.ventana_calc, text = "(", width= 6, padx = 10, pady = 5, command= lambda: click_boton("("))
        boton_parent1.grid(row= 3, column= 1)

        boton_parent2 = tk.Button(self.ventana_calc, text = ")", width= 6, padx = 10, pady = 5, command= lambda: click_boton(")"))
        boton_parent2.grid(row= 3, column= 2)

        botonAC = tk.Button(self.ventana_calc, text = "AC", width= 6, bg = "Orange", padx = 10, pady = 5, command= lambda: borrar())
        botonAC.grid(row= 3, column= 0)

        #botones de operaciones

        boton_suma = tk.Button(self.ventana_calc, text = "+", width= 6, padx = 10, pady = 5, command= lambda: click_boton("+"))
        boton_suma.grid(row= 3, column= 3)

        boton_rest = tk.Button(self.ventana_calc, text = "-", width= 6, padx = 10, pady = 5, command= lambda: click_boton("-"))
        boton_rest.grid(row= 4, column= 3)

        boton_mult = tk.Button(self.ventana_calc, text = "X", width= 6, padx = 10, pady = 5, command= lambda: click_boton("*"))
        boton_mult.grid(row= 5, column= 3)

        boton_div = tk.Button(self.ventana_calc, text = "/", width= 6, padx = 10, pady = 5, command= lambda: click_boton("/"))
        boton_div.grid(row= 6, column= 3)

        boton_igual = tk.Button(self.ventana_calc, text = "=", width= 6, padx = 10, pady = 5, command= lambda : operacion())
        boton_igual.grid(row= 7, column= 3)

        boton_punto = tk.Button(self.ventana_calc, text= ".", width= 6, padx= 10, pady= 5, command= lambda: click_boton("."))
        boton_punto.grid(row= 7, column= 2)


        self.ventana_calc.mainloop()
        








   

    #MARK: CONVERSOR DE UNIDADES
    def conversor_de_unidades(self):
        self.try_to_destroy_ventanas()
        #inicializaciones
        self.ventana_conversor_de_unidades =tk.Tk() 
        self.ventana_conversor_de_unidades.title('Conversor de unidades. Codigo abierto.')
        #moneda
        self.frame_moneda = ttk.LabelFrame(self.ventana_conversor_de_unidades, text='MONEDAS',)
        self.frame_moneda.grid(row=0, column=0, sticky='NS', padx=50, pady=50) #frame moneda, utilizar el padx y pady igual para los demas frames
        quiero_convertir_label = ttk.Label(self.frame_moneda, text='Quiero convertir:',)
        quiero_convertir_label.grid(row=1, column=0,)
        self.entry_moneda1 = ttk.Entry(self.frame_moneda,)
        self.entry_moneda1.grid(row=2, column=0, columnspan=2, sticky='EW') #columnspan standarizado
        #menu desplegable moneda1
        self.selected_option_moneda1 = tk.StringVar() #almacenar seleccion
        self.menu_desplegable_moneda1 = ttk.Combobox(
            self.frame_moneda,
            textvariable=self.selected_option_moneda1,
            state="readonly",
            values=["euro, €", "dolar, $", "peseta"]
        )

        self.menu_desplegable_moneda1.grid(row=3, column=0, pady=5)
        a = ttk.Label(self.frame_moneda, text='A:',)
        a.grid(row=4, column=0,)
        #menu desplegable moneda 2 (el segundo menu desplegable)
        self.selected_option_moneda2 = tk.StringVar() #almacenar seleccion
        self.menu_desplegable_moneda2 = ttk.Combobox(
            self.frame_moneda,
            textvariable=self.selected_option_moneda2,
            state="readonly",
            values=["euro, €", "dolar, $", "peseta",]
        )
        self.menu_desplegable_moneda2.grid(row=5, column=0, pady=5)

        self.entry_resultado_moneda = ttk.Entry(self.frame_moneda, )
        self.entry_resultado_moneda.grid(row=6, column=0, columnspan=2, sticky='EW')
        self.boton_resultado_moneda = ttk.Button(self.frame_moneda, command=self.calcular_conversor_de_unidades, text='Calcular')
        self.boton_resultado_moneda.grid(row=7, column=0, pady=0)
        #DISTANCIA
        self.frame_distancia = ttk.LabelFrame(self.ventana_conversor_de_unidades, text='DISTANCIA',)
        self.frame_distancia.grid(row=0, column=1, sticky='NS', padx=50, pady=50) #frame moneda, utilizar el padx y pady igual para los demas frames
        quiero_convertir_label2 = ttk.Label(self.frame_distancia, text='Quiero convertir:',)
        quiero_convertir_label2.grid(row=1, column=0,)
        self.entry_distancia1 = ttk.Entry(self.frame_distancia,)
        self.entry_distancia1.grid(row=2, column=0, columnspan=2, sticky='EW') #columnspan standarizado
        #menu desplegable distancia1
        self.selected_option_distancia1 = tk.StringVar() #almacenar seleccion
        self.menu_desplegable_distancia1 = ttk.Combobox(
            self.frame_distancia,
            textvariable=self.selected_option_distancia1,
            state="readonly",
            values=["SISTEMA METRICO","mm", "cm", "m", "km", "SISTEMA IMPERIAL", "pulgada", "pie", "yarda", "milla", ]
        )

        self.menu_desplegable_distancia1.grid(row=3, column=0, pady=5)
        a2 = ttk.Label(self.frame_distancia, text='A:',)
        a2.grid(row=4, column=0,)
        #menu desplegable moneda 2 (el segundo menu desplegable)
        self.selected_option_distancia2 = tk.StringVar() #almacenar seleccion
        self.menu_desplegable_distancia2 = ttk.Combobox(
            self.frame_distancia,
            textvariable=self.selected_option_distancia2,
            state="readonly",
            values=["SISTEMA METRICO","mm", "cm", "m", "km", "SISTEMA IMPERIAL", "pulgada", "pie", "yarda", "milla", ]
        )
        self.menu_desplegable_distancia2.grid(row=5, column=0, pady=5)

        self.entry_resultado_distancia = ttk.Entry(self.frame_distancia, )
        self.entry_resultado_distancia.grid(row=6, column=0, columnspan=2, sticky='EW')
        self.boton_resultado_distancia = ttk.Button(self.frame_distancia, command=self.calcular_conversor_de_unidades, text='Calcular')
        self.boton_resultado_distancia.grid(row=7, column=0, pady=0)

        aviso_conversor = ttk.Label(self.ventana_conversor_de_unidades, text="Datos de el conversor de monedas actualizado a 11/12/2023", padding=(0, 0, 0, 0))
        aviso_conversor.grid(row=1)


    def calcular_conversor_de_unidades(self):
        #moneda
        if self.menu_desplegable_moneda1.get() == "euro, €" and self.menu_desplegable_moneda2.get() == "dolar, $":
            self.entry_resultado_moneda.delete(0, tk.END)
            self.entry_resultado_moneda.insert(0, int(self.entry_moneda1.get()) * 1.07560,)
        elif self.menu_desplegable_moneda1.get() =="dolar, $" and self.menu_desplegable_moneda2.get() == "euro, €":
            self.entry_resultado_moneda.delete(0, tk.END)
            self.entry_resultado_moneda.insert(0, int(self.entry_moneda1.get()) / 1.07560,)
        
        if self.menu_desplegable_moneda1.get() == "euro, €" and self.menu_desplegable_moneda2.get() == "peseta":
            self.entry_resultado_moneda.delete(0, tk.END)
            self.entry_resultado_moneda.insert(0, int(self.entry_moneda1.get()) * 166.386)
        elif self.menu_desplegable_moneda1.get() == "peseta" and self.menu_desplegable_moneda2.get() == "euro, €":
            self.entry_resultado_moneda.delete(0, tk.END)
            self.entry_resultado_moneda.insert(0, int(self.entry_moneda1.get()) / 166.386)

        if self.menu_desplegable_moneda1.get() == "dolar, $" and self.menu_desplegable_moneda2.get() == "peseta":
            self.entry_resultado_moneda.delete(0, tk.END)
            self.entry_resultado_moneda.insert(0, int(self.entry_moneda1.get()) * 166.94000)
        elif self.menu_desplegable_moneda1.get() == "peseta" and self.menu_desplegable_moneda2.get() == "dolar, $":
            self.entry_resultado_moneda.delete(0, tk.END)
            self.entry_resultado_moneda.insert(0, int(self.entry_moneda1.get()) / 166.94000)
        #distancia
        if self.menu_desplegable_distancia1.get() == "mm" and self.menu_desplegable_distancia2.get() == "pulgada":
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 0.0393701)
        elif self.menu_desplegable_distancia1.get() == 'pulgada' and self.menu_desplegable_distancia2.get() == 'mm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) /0.0393701)

        elif self.menu_desplegable_distancia1.get() == 'mm' and self.menu_desplegable_distancia2.get() == 'pie':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 0.00328084)
        elif self.menu_desplegable_distancia1.get() == 'pie' and self.menu_desplegable_distancia2.get() == 'mm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 0.00328084)

        elif self.menu_desplegable_distancia1.get() == 'mm' and self.menu_desplegable_distancia2.get() == 'yarda':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 0.00109361)
        elif self.menu_desplegable_distancia1.get() == 'yarda' and self.menu_desplegable_distancia2.get() == 'mm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 0.00109361)
        #distancia IA
        elif self.menu_desplegable_distancia1.get() == 'mm' and self.menu_desplegable_distancia2.get() == 'cm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 10)
        elif self.menu_desplegable_distancia1.get() == 'cm' and self.menu_desplegable_distancia2.get() == 'mm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 10)

        elif self.menu_desplegable_distancia1.get() == 'mm' and self.menu_desplegable_distancia2.get() == 'm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 1000)
        elif self.menu_desplegable_distancia1.get() == 'm' and self.menu_desplegable_distancia2.get() == 'mm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 1000)

        elif self.menu_desplegable_distancia1.get() == 'mm' and self.menu_desplegable_distancia2.get() == 'km':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 1000000)
        elif self.menu_desplegable_distancia1.get() == 'km' and self.menu_desplegable_distancia2.get() == 'mm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 1000000)

        elif self.menu_desplegable_distancia1.get() == 'pulgada' and self.menu_desplegable_distancia2.get() == 'pie':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 12)
        elif self.menu_desplegable_distancia1.get() == 'pie' and self.menu_desplegable_distancia2.get() == 'pulgada':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 12)

        elif self.menu_desplegable_distancia1.get() == 'pulgada' and self.menu_desplegable_distancia2.get() == 'yarda':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 36)
        elif self.menu_desplegable_distancia1.get() == 'yarda' and self.menu_desplegable_distancia2.get() == 'pulgada':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 36)

        elif self.menu_desplegable_distancia1.get() == 'cm' and self.menu_desplegable_distancia2.get() == 'm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 100)
        elif self.menu_desplegable_distancia1.get() == 'm' and self.menu_desplegable_distancia2.get() == 'cm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 100)

        elif self.menu_desplegable_distancia1.get() == 'cm' and self.menu_desplegable_distancia2.get() == 'km':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 100000)
        elif self.menu_desplegable_distancia1.get() == 'km' and self.menu_desplegable_distancia2.get() == 'cm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 100000)

        elif self.menu_desplegable_distancia1.get() == 'm' and self.menu_desplegable_distancia2.get() == 'km':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 1000)
        elif self.menu_desplegable_distancia1.get() == 'km' and self.menu_desplegable_distancia2.get() == 'm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 1000)

        elif self.menu_desplegable_distancia1.get() == 'pie' and self.menu_desplegable_distancia2.get() == 'yarda':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 3)
        elif self.menu_desplegable_distancia1.get() == 'yarda' and self.menu_desplegable_distancia2.get() == 'pie':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 3)
        elif self.menu_desplegable_distancia1.get() == 'mm' and self.menu_desplegable_distancia2.get() == 'milla':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 6.21371e-7)
        elif self.menu_desplegable_distancia1.get() == 'milla' and self.menu_desplegable_distancia2.get() == 'mm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 6.21371e-7)

        
        elif self.menu_desplegable_distancia1.get() == 'pulgada' and self.menu_desplegable_distancia2.get() == 'milla':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 1.57828e-5)
        elif self.menu_desplegable_distancia1.get() == 'milla' and self.menu_desplegable_distancia2.get() == 'pulgada':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 1.57828e-5)

        elif self.menu_desplegable_distancia1.get() == 'pie' and self.menu_desplegable_distancia2.get() == 'milla':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 0.000189394)
        elif self.menu_desplegable_distancia1.get() == 'milla' and self.menu_desplegable_distancia2.get() == 'pie':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 0.000189394)

        elif self.menu_desplegable_distancia1.get() == 'yarda' and self.menu_desplegable_distancia2.get() == 'milla':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 0.000568182)
        elif self.menu_desplegable_distancia1.get() == 'milla' and self.menu_desplegable_distancia2.get() == 'yarda':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 0.000568182)

        elif self.menu_desplegable_distancia1.get() == 'cm' and self.menu_desplegable_distancia2.get() == 'pulgada':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 0.393701)
        elif self.menu_desplegable_distancia1.get() == 'pulgada' and self.menu_desplegable_distancia2.get() == 'cm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 0.393701)

        elif self.menu_desplegable_distancia1.get() == 'cm' and self.menu_desplegable_distancia2.get() == 'pie':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 0.0328084)
        elif self.menu_desplegable_distancia1.get() == 'pie' and self.menu_desplegable_distancia2.get() == 'cm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 0.0328084)

        elif self.menu_desplegable_distancia1.get() == 'cm' and self.menu_desplegable_distancia2.get() == 'yarda':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 0.0109361)
        elif self.menu_desplegable_distancia1.get() == 'yarda' and self.menu_desplegable_distancia2.get() == 'cm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 0.0109361)

        elif self.menu_desplegable_distancia1.get() == 'cm' and self.menu_desplegable_distancia2.get() == 'milla':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 6.21371e-6)
        elif self.menu_desplegable_distancia1.get() == 'milla' and self.menu_desplegable_distancia2.get() == 'cm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 6.21371e-6)

        elif self.menu_desplegable_distancia1.get() == 'm' and self.menu_desplegable_distancia2.get() == 'pulgada':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 39.3701)
        elif self.menu_desplegable_distancia1.get() == 'pulgada' and self.menu_desplegable_distancia2.get() == 'm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 39.3701)

        elif self.menu_desplegable_distancia1.get() == 'm' and self.menu_desplegable_distancia2.get() == 'pie':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 3.28084)
        elif self.menu_desplegable_distancia1.get() == 'pie' and self.menu_desplegable_distancia2.get() == 'm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 3.28084)

        elif self.menu_desplegable_distancia1.get() == 'm' and self.menu_desplegable_distancia2.get() == 'yarda':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 1.09361)
        elif self.menu_desplegable_distancia1.get() == 'yarda' and self.menu_desplegable_distancia2.get() == 'm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 1.09361)

        elif self.menu_desplegable_distancia1.get() == 'm' and self.menu_desplegable_distancia2.get() == 'milla':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 0.000621371)
        elif self.menu_desplegable_distancia1.get() == 'milla' and self.menu_desplegable_distancia2.get() == 'm':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 0.000621371)

        elif self.menu_desplegable_distancia1.get() == 'km' and self.menu_desplegable_distancia2.get() == 'pulgada':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 39370.1)
        elif self.menu_desplegable_distancia1.get() == 'pulgada' and self.menu_desplegable_distancia2.get() == 'km':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 39370.1)

        elif self.menu_desplegable_distancia1.get() == 'km' and self.menu_desplegable_distancia2.get() == 'pie':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 3280.84)
        elif self.menu_desplegable_distancia1.get() == 'pie' and self.menu_desplegable_distancia2.get() == 'km':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 3280.84)

        elif self.menu_desplegable_distancia1.get() == 'km' and self.menu_desplegable_distancia2.get() == 'yarda':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 1093.61)
        elif self.menu_desplegable_distancia1.get() == 'km' and self.menu_desplegable_distancia2.get() == 'milla':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) * 0.621371)
        elif self.menu_desplegable_distancia1.get() == 'milla' and self.menu_desplegable_distancia2.get() == 'km':
            self.entry_resultado_distancia.delete(0, tk.END)
            self.entry_resultado_distancia.insert(0, int(self.entry_distancia1.get()) / 0.621371)
            
        
        

        
        









class airstrike_company_balistik(tk.Toplevel): #MARK: CLASS airstrike_company_BALISTIK
    


    def __init__(self):
        super().__init__()
        self.configure(bg='Grey20')
        self.geometry("500x450")
        self.title('airstrike_company balistick rocket launching softwar. ')
        _title = tk.Label(self, text= "Wellcome to the airstrike_company ballistic rocket launching software", font= "Small_fonts_normal", bg= "yellow")
        _title.grid(row= 0, column= 0, columnspan= 4)

        _title2 = tk.Label(self, text= "please imput coordinates for rocket launching site and press button to continue", font= "Small_fonts_normal 10", bg= "yellow")
        _title2.grid(row=1, column=0, columnspan= 4)

        self.e_texto = tk.Entry(self, font = "Arial 20", bg= "DarkGoldenrod1")
        self.e_texto.grid(row = 2, column = 0, columnspan = 4, padx = 100, pady = 20) 

        self.boton1 = tk.Button(self, text= "CONTINUE", bg= "Yellow", command= self.abrir_nueva_ventana)
        self.boton1.grid(row= 3, column= 1, columnspan= 2)
        self.entry_var = tk.StringVar()
        self.place_holder_text = 'ENTER THE PASSWORD' #ENTER THE PASSWORD NO SE INSERTAAAAAAAAAAAAAAAA
        self.mainloop()
        
    def crear_e_texto(self):
        self.e_texto = tk.Entry(self, font = "Arial 20", bg= "DarkGoldenrod1")
        self.e_texto.grid(row = 2, column = 0, columnspan = 4, padx = 100, pady = 20) 
    def abrir_nueva_ventana(self):
        self.nueva_ventanaa = tk.Toplevel()
        self.nueva_ventanaa.title("ENTER THE PASSWORD")
        self.nueva_ventanaa.geometry("500x450")
        self.nueva_ventanaa.configure(bg="grey20")
        
        self.e_textoi = ttk.Entry(self.nueva_ventanaa, font = "Arial 20", textvariable=self.entry_var, style='placeholder.TEntry') #bg= "DarkGoldenrod1" para tk #entry ttk que cuando le clickeas desaparece el texto
        self.e_textoi.grid(row = 0, column = 0, columnspan = 4, padx = 100, pady = 20, ipadx=10)
        self.e_textoi.bind("<FocusIn>", self.entry_focus_in)
        self.e_textoi.bind("<FocusOut>", self.entry_focus_out)
        self.e_textoi.insert(0, self.place_holder_text)
    

        self.boton_launch = tk.Button(self.nueva_ventanaa, text = "LAUNCH", width= 6, padx = 140, pady = 5, bg= "red4", command=self.init_operacion2) #comand no inicia directamente el metodo operacion2
        self.boton_launch.grid(row=1, column=1, columnspan= 2)
        
        self.boton1.config(state='disable') 
        def close_nueva_ventana():
            self.nueva_ventanaa.destroy()
            self.boton1.config(state='normal')
            
        self.nueva_ventanaa.protocol('WM_DELETE_WINDOW', close_nueva_ventana)        
        
    
    def init_operacion2(self):
        self.boton_launch.config(state='disable')
        self.execute_operacion2 = True
        self.operacion2()
    def operacion2(self):
        if self.execute_operacion2 == True:
            code =self.e_textoi.get()
            if code == '8571': #esperar 3 segundos antes de crear la nueva ventana que indique que el objetivo ha sido destruido
                self.place_holder_text = 'LAUNCHING'
                self.e_textoi.delete(0, tk.END)
                self.e_textoi.insert(0, self.place_holder_text)

                self.nueva_ventanaa.after(3000, self.crear_nueva_ventana_done) #aqui se espera
            elif code == '':
                self.place_holder_text='ENTER THE PASSWORD'
                self.e_textoi.delete(0, tk.END)
                self.e_textoi.insert(0, self.place_holder_text)
            elif code != '  ':
                self.place_holder_text = 'WRONG CODE'
                self.e_textoi.delete(0, tk.END)
                self.e_textoi.insert(0,self.place_holder_text)
            
    def crear_nueva_ventana_done(self):
        self.nueva_ventana_done = tk.Toplevel()
        self.nueva_ventana_done.configure(bg='Grey20')
        self.nueva_ventana_done.title('Done')

        _label_done = tk.Label(self.nueva_ventana_done, text='Objective has been destroyed', font= "Small_fonts_normal", bg= "yellow")
        _label_done.pack()
    #focusin-focusout
    def entry_focus_in(self, event):
        if self.entry_var.get() == self.place_holder_text:
            self.entry_var.set("")
    def entry_focus_out(self, event):
        if self.entry_var.get() == "":
            self.entry_var.set(self.place_holder_text)

        
        
    #ENTRY DE TEXTO
    
    def operacion(self):
        ecuacion =self.e_texto.get()
    

    

    
    
        
    
        

    
        




if __name__ == '__main__':
    window = tk.Tk()
    application = Cuerpo(window)
    window.mainloop()





#errores que tengo que arreglar que he encontrado en este proyecto

    #divdir la clase entre funciones y atributos y no poner el codigo suelto dentro de innit
    #acordarse de poner cosas privadas para ordenar
    #repasar fundamentos POO python antes de empezar un proyecto
    #poner todo en funciones
