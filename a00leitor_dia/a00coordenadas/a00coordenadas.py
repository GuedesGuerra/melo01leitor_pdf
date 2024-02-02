class CoordenadasGia:
        def __init__(self):
            self.a00mes_ano_referencia = (350, 120, 550, 135)
            self.a01nome_empresarial = (30, 150, 550, 165)
            self.a02sem_st_com_exterior34 = (375, 335, 460, 345)
            self.a03sem_st_com_exterior44 = (480, 335, 570, 345)
            self.a04outros39 = (480, 335, 570, 345)
            self.a05outros49 = (480, 410, 570, 420)
            self.a06total40 = (375, 422, 465, 434)
            self.a07total50 = (480, 422, 570, 434)
            self.a08por_saida_com_debito_imposto = (230, 450, 290, 470)

        def _coordenadas_gia(self):
            self.CoordenadasGia = {"coord_gia":[self.a00mes_ano_referencia, self.a01nome_empresarial, self.a02sem_st_com_exterior34, self.a03sem_st_com_exterior44,
            self.a04outros39, self.a05outros49, self.a06total40, self.a07total50, self.a08por_saida_com_debito_imposto]}
            return self.CoordenadasGia

        # def __init__(self):
        #     self.a00mes_ano_referencia = (350, 120, 550, 130)
        #     self.a01nome_empresarial = (30, 150, 550, 160)
        #     self.a02sem_st_no_estado = (380, 300, 500, 310)
        #     self.a03sem_st_com_outros_estado = (380, 315, 470, 329)
        #     self.a04total = (375, 422, 465, 434)
        #     self.a05por_saida_com_debito_imposto = (230, 450, 290, 470)