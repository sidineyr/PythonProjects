from formatapendrivelinux import extrair_particoes_seguras


def test_exibe_so_particao_removivel_gravavel_e_desmontada():
    dados = {
        "blockdevices": [
            {
                "path": "/dev/sda",
                "type": "disk",
                "rm": False,
                "ro": False,
                "model": "Disco interno",
                "children": [
                    {
                        "path": "/dev/sda1",
                        "type": "part",
                        "rm": False,
                        "ro": False,
                        "size": "100G",
                        "mountpoints": ["/"],
                    }
                ],
            },
            {
                "path": "/dev/sdb",
                "type": "disk",
                "rm": True,
                "ro": False,
                "model": "Pendrive de teste",
                "children": [
                    {
                        "path": "/dev/sdb1",
                        "type": "part",
                        "rm": True,
                        "ro": False,
                        "size": "16G",
                        "mountpoints": [None],
                    },
                    {
                        "path": "/dev/sdb2",
                        "type": "part",
                        "rm": True,
                        "ro": False,
                        "size": "1G",
                        "mountpoints": ["/media/usuario/USB"],
                    },
                ],
            },
            {
                "path": "/dev/sdc",
                "type": "disk",
                "rm": True,
                "ro": True,
                "children": [
                    {
                        "path": "/dev/sdc1",
                        "type": "part",
                        "rm": True,
                        "ro": True,
                        "mountpoints": [None],
                    }
                ],
            },
        ]
    }

    assert extrair_particoes_seguras(dados) == [
        {
            "path": "/dev/sdb1",
            "size": "16G",
            "model": "Pendrive de teste",
        }
    ]


def test_rejeita_caminho_de_dispositivo_com_subdiretorio():
    dados = {
        "blockdevices": [
            {
                "path": "/dev/disk/by-id/usb-exemplo",
                "type": "part",
                "rm": True,
                "ro": False,
                "mountpoints": [None],
            }
        ]
    }

    assert extrair_particoes_seguras(dados) == []
