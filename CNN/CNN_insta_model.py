from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import numpy as np
import tensorflow as tf
class CNN_insta:

    def __init__(self, file, model = '/content/drive/My Drive/Data/cnn_insta_fit.h5'):
        self.model = model
        self.file = file

    def image_to_numpy(self):
        categories = ["eat", "cat", "cloth"]
        image_w = 32
        image_h = 32
        X = []

        img = Image.open(self.file)
        img = img.convert("RGB")
        img = img.resize((image_w, image_h))
        data = np.asarray(img) / 255
        X.append(data)
        X.append(data)
        X = np.array(X)
        return X

    def classify_image(self):
        categories = ["Eat", "Cat", "Cloth"]

        model = tf.keras.models.load_model(self.model)
        y = model.predict_classes(CNN_insta.image_to_numpy(self))
        return categories[y[0]]

    def recommend_tags(self):
        categories = CNN_insta.classify_image(self)
        if categories == 'Eat':
            return ['맛스타그램','먹스타그램','일상','맛집','데일리','먹방','daily','일상스타그램','food','데일리그램','foodstagram','럽스타그램','인스타그램','푸드스타그램','여행','홍대','주말','instafood','먹스타','jmt'],['과자','아가리어터','후기','리뷰','디엠','과자스타그램','친구스타그램','서면술집추천','남매스타그램','그집뱃살','중마동카페','순천마카롱','중마동마카롱','맛있게먹으면0칼로리','광양카페','인스타사','순천카페','홍대카페','흑돼지','봄']
        elif categories == 'Cat':
            return ['집사스타그램','냥스타그램','고양이','cat','catstagram','집사','캣스타그램','반려묘','일상','고양이그램','고양이스타그램','개냥이','냥이','미묘','집사그램','데일리','daily','아깽이','반려동물','사지말고입양하세요'],['감자스타그램','꽃으로도때리지마세요','photography','치즈코숏','댕냥이','해피펫아카데미','뉴스1','halloween','집사님맞팔','야생동물','nekostagram','맹수','dogs','반려동물여행','먼치킨나폴레옹','엑죠틱','해피펫','집스타그램','해운대','꽃집고양이']
        else:
            return ['데일리룩','ootd','일상','오오티디','데일리','셀카','패션','셀스타그램','셀피','패션스타그램','daily','dailylook','얼스타그램','selfie','fashion','데일리코디','코디','옷','스타일'],['남자가을옷','팔찌','btsarmy','silver','20대여자쇼핑몰','indonesia','여주','커플링','着画','旅行','スタイル','화이트','美容','woman','일산옷가게','패딩조끼','목걸이','반지','스톤아일랜드패딩','корейскиймакияж']
