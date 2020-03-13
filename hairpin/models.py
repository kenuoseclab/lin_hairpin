from django.db import models

PLAIN_CAMI = 1  # 普通卡密
REPEAT_CAMI = 2  # 重复卡密

CAMI_TYPE_MAP = {
    PLAIN_CAMI: '普通卡密',
    REPEAT_CAMI: '重复卡密'
}


class Category(models.Model):
    """
    产品分类
    """
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=50, verbose_name='分类名称')

    desc = models.CharField(max_length=100, verbose_name='分类描述', blank=True, null='')

    class Meta:

        db_table = 'category'
        verbose_name = '产品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '分类: ' + self.title


class Product(models.Model):
    """
    产品表
    """
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=100, verbose_name='产品名称')

    price = models.FloatField(default=1.00, verbose_name='销售价格(元)')

    cami_type = models.PositiveSmallIntegerField(default=PLAIN_CAMI, verbose_name='卡密类型')

    desc = models.CharField(max_length=100, verbose_name='商品描述', blank=True, null='')

    status = models.BooleanField(verbose_name='上架状态', default=True) # True上架，否则下架

    category = models.ForeignKey("Category", verbose_name='分类', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'
        verbose_name = '产品列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '产品: ' + self.title


class Cami(models.Model):
    """
    卡密表
    """
    id = models.AutoField(primary_key=True)

    product = models.ForeignKey("Product", verbose_name='产品', on_delete=models.CASCADE)

    card_no = models.CharField(max_length=255, blank=True, null='', verbose_name='卡号')

    card_pwd = models.CharField(max_length=255, blank=True, null='', verbose_name='卡密')

    status = models.BooleanField(verbose_name='状态', default=0)  # 0未出售, 1已出售

    class Meta:

        db_table = 'cami'
        verbose_name = '卡密列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '商品: ' + self.product.title + '卡密'


class PayRecord(models.Model):
    """
    支付记录表
    """
    id = models.AutoField(primary_key=True)

    pay_no = models.CharField(max_length=100, unique=True, verbose_name='支付单号')

    pay_money = models.FloatField(verbose_name='支付金额')

    pay_time = models.DateTimeField(verbose_name='支付时间')

    status = models.BooleanField(verbose_name='支付状态', default=False)  # 支付是否成功

    class Meta:
        db_table = 'pay_record'
        verbose_name = '支付记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '支付单号:' + self.pay_no


class Order(models.Model):
    """
    订单记录表
    """
    id = models.AutoField(primary_key=True)

    order_no = models.CharField(max_length=100, verbose_name='订单号')

    pay_record = models.ForeignKey("PayRecord", verbose_name='支付记录', on_delete=models.CASCADE)

    product = models.ForeignKey("Product", verbose_name='商品', on_delete=models.CASCADE)

    cami = models.ForeignKey("Cami", verbose_name='卡密', on_delete=models.CASCADE)

    status = models.PositiveSmallIntegerField(verbose_name='订单状态', default=0)  # 0 等待支付, 1待提取, 2 已完成

    class Meta:
        db_table = 'order'
        verbose_name = '订单记录'
        verbose_name_plural = verbose_name


    def __str__(self):
        return '订单号:' + self.order_no