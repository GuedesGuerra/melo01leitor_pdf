class CoordenadasGia:
        def __init__(self):
            self.a00mes_ano_referencia = (350, 120, 550, 130)
            self.a01nome_empresarial = (30, 150, 550, 160)
            self.a02sem_st_no_estado = (480, 305, 600, 317)
            self.a03sem_st_com_outros_estado = (480, 317, 600, 329)
            self.a04total = (375, 422, 465, 434)
            self.a05por_saida_com_debito_imposto = (230, 450, 290, 470)

        def _coordenadas_gia(self):
            self.CoordenadasGia = {"coord_gia":[self.a00mes_ano_referencia, self.a01nome_empresarial, self.a02sem_st_no_estado, self.a03sem_st_com_outros_estado, 
            self.a04total, self.a05por_saida_com_debito_imposto]}
            return self.CoordenadasGia