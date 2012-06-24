#
# TODO:
# - fix descriptions and summaries to reflect that it isn't rsync but rsyncrypto
#
Summary:	Program for efficient remote updates of files
Summary(es):	Programa para actualizar archivos remotos de forma eficiente
Summary(ko):	��Ʈ��ũ�� ���� ���ϵ���ȭ�� ���� ���α׷�
Summary(pl):	Program do wydajnego zdalnego uaktualniania plik�w
Summary(pt_BR):	Programa para atualizar arquivos remotos de forma eficiente
Summary(ru):	��������� ��� ������������ ���������� ���������� ������
Summary(uk):	�������� ��� ����������� צ��������� ��������� ���̦�
Summary(zh_CN):	[ͨѶ]���乤��
Summary(zh_TW):	[���]$(B6G?i��(c(B
Name:		rsyncrypto
Version:	0.17
Release:	0.5
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/rsyncrypto/%{name}-%{version}.tar.gz
# Source0-md5:	b04df4561d5f9847b647f9c60912d2af
URL:		http://rsync.samba.org/
BuildRequires:	argtable2-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	openssl-devel
Requires:	gzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rsync is a replacement for rcp that has many more features.

rsync uses the "rsync algorithm" which provides a very fast method for
bringing remote files into sync. It does this by sending just the
differences in the files across the link, without requiring that both
sets of files are present at one of the ends of the link beforehand.

A technical report describing the rsync algorithm is included with
this package.

%description -l es
rsync es un substituto m�s r�pido y flexible para rcp que permite la
sincronizaci�n de archivos o directorios, v�a red, de forma r�pida y
eficiente, entre diferentes m�quinas transfiriendo solamente las
diferencias entre estos directorios de forma compactada. No necesita
que ninguna de las m�quinas tengan una copia de lo que est� en la
otra. Est� disponible en este paquete, una relaci�n t�cnica
describiendo el algoritmo usado por el rsync.

%description -l ko
Rsync�� ���� ȣ��Ʈ ������ �ſ� ���� ����ȭ�ϴµ� �ŷ��Ҹ���
�˰����� ����Ѵ�. Rsync�� ������ ��ü�� ������ �� ��ſ� ��Ʈ����
���� ������ �ٸ� �κи��� �����ϱ� ������ ������. Rsync�� ������ �̷�
���μ��� Ȥ�� rcp Ŀ��带 ���� �� ����� ��ü�����ν� ���ȴ�. rsync
�˰����� �����ϴ� ������� ������ �� �ٷ��̿� ���ԵǾ� �ִ�.

%description -l pl
Rsync jest zamiennikiem programu rcp z bardziej rozbudowan� sk�adni�
polece�. Program ten u�ywa efektywnego algorytmu "rsync" w czasie
komunikacji i transportu plik�w do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu zosta�a r�wnie� do��czona do pakietu.

%description -l pt_BR
O rsync � um substituto mais r�pido e flex�vel para o rcp permitindo
sincroniza��o de arquivos ou diret�rios via rede de forma r�pida e
eficiente entre diferentes m�quinas transferindo somente as diferen�as
entre estes diret�rios de forma compactada. Ele n�o precisa que
nenhuma das m�quinas tenha uma c�pia do que est� na outra.

Um relat�rio t�cnico descrevendo o algoritmo usado pelo rsync est�
dispon�vel neste pacote.

%description -l ru
rsync - ��� ����� ������� � ������ ������������ rcp, �����������
������� � ����������� �� ��������� � �������� ���� �������������
������ ��� ��������� �� ��������� ������� ����� �������� ������
�������� ����� ���� � ����������������� ����. ��� ���� ���������� ��
�����������, ����� ���� ������ ����� � ���� ����� ����, ��� ���� ��
������ ������.

%description -l uk
rsync - �� ������ �� ����˦�� ������������ rcp, ��� ��������դ ������
�� ��������� �� צ�������� �� �����Ӧ� ����֦ ������Φ��æ� ���̦� ��
������Ǧ� �� Ҧ���� ������� ������ ������ަ ���� צ�ͦ������� ͦ� ����
� �������������� ��Ħ. ��� ����� ���Ӧ� �� ����'������, ��� ����
������ ���� � ���� ��Ц� ����, �� � �� ��ۦ� ����Φ.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%{__autoheader}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
