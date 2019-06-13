from django.db import models


class PersonalInfo(models.Model):
    name = models.CharField(max_length=55, verbose_name="Name and Surname", blank="False")
    degree = models.CharField(max_length=55, verbose_name="Your Position", blank="False")
    image = models.ImageField(blank="True")
    birthday = models.DateField()
    placeofbirth = models.CharField(max_length=55, verbose_name="Place of Birth")
    mail = models.EmailField(verbose_name="Your Mail Adress", blank="False")
    phone = models.IntegerField(verbose_name="Your Phone Number", blank="True")
    city = models.CharField(max_length=55, verbose_name="City", blank="True")

    class Meta:
        verbose_name_plural = "1 - Personal Infos"
        verbose_name = "Personal Info"


class Section(models.Model):
    title = models.CharField(max_length=255, verbose_name='Section Title', blank="True", default='')

    class Meta:
        verbose_name_plural = "2 - Sections"
        verbose_name = "Section"
        ordering = ['title']

    def __str__(self):
        return self.title


class Content(models.Model):
    DATE_CHOISES=(
        ('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'),
        ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'),
        ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'),
        ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'),
        ('2014', '2014'), ('2015', '2015'), ('2016', '2017'), ('2018', '2019'), ('2020', '2020'), ('2021', '2021'),
        ('now', 'now'),
    )
    section = models.ForeignKey('home.Section', related_name='content_section', verbose_name='Section', on_delete=models.CASCADE, default='', blank=False)
    title = models.CharField(max_length=255, verbose_name='Data Title', default='')
    startdate = models.CharField(max_length=25, choices=DATE_CHOISES, blank="True", verbose_name="Start Date")
    enddate = models.CharField(max_length=25, choices=DATE_CHOISES, blank="True", verbose_name="End Date")
    image = models.ImageField(blank="False")
    institution = models.CharField(max_length=255, verbose_name='Institution Name', blank="True")
    faculty = models.CharField(max_length=255, verbose_name='Faculty Name', blank="True")
    department = models.CharField(max_length=255, verbose_name='Department Name', default='', blank="True")
    city = models.CharField(max_length=25, verbose_name='City Name', null=True, blank="True")

    class Meta:
        verbose_name_plural = "3 - Contents"
        verbose_name = "Content"
        ordering = ['section__title', 'title']

    def __str__(self):
        return self.title


class FooterText(models.Model):
    text = models.CharField(max_length=255, verbose_name='Text', blank=True)

    class Meta:
        verbose_name_plural = '4 - Footer Texts'
        verbose_name = 'Footer Text'

    def __str__(self):
        return self.text


class Social(models.Model):
    SOCIAL_CHOISES=(
        ('Facebook-f', 'facebook'), ('Twitter', 'twitter'), ('Instagram', 'instagram'), ('Whatsapp', 'whatsapp'), ('youtube', 'youtube')
    )
    title = models.CharField(max_length=99, choices=SOCIAL_CHOISES, verbose_name='Select Social Media', blank=False)
    username = models.CharField(max_length=99, verbose_name='Username', blank=False)
    link = models.URLField(verbose_name='URL')

    class Meta:
        verbose_name_plural = '5 - Social Accounts'
        verbose_name = 'Social Account'
        ordering = ['username', 'title']

    def __str__(self):
        return "{0} - {1}".format(self.title, self.username)
