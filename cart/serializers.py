from decimal import Decimal

from rest_framework import serializers

from .models import CartItem
from beads.models import Bead
from colors.models import Color
from disks.models import Disk


class CartItemSerializer(serializers.ModelSerializer):

    ALLOWED_BEAD_SIZES = {4, 6, 8, 10}

    class Meta:
        model = CartItem
        fields = "__all__"

        read_only_fields = [
            "id",
            "user",
            "bead",
            "color",
            "disk",
            "total_price",
            "created_at",
        ]

    # =========================================================
    # VALIDATE CONFIGURATION
    # =========================================================

    def validate_configuration(self, configuration):

        if not isinstance(configuration, dict):
            raise serializers.ValidationError(
                "Configuration must be an object."
            )

        # =====================================================
        # BEADS
        # =====================================================

        beads = configuration.get("beads")

        if not isinstance(beads, list) or len(beads) == 0:
            raise serializers.ValidationError({
                "beads": "At least one bead is required."
            })

        # =====================================================
        # GLOBAL BEAD SIZE
        # =====================================================

        bead_size_mm = configuration.get("bead_size_mm")

        if bead_size_mm is None:
            raise serializers.ValidationError({
                "bead_size_mm": "Bead size is required."
            })

        try:
            bead_size_mm = int(bead_size_mm)

        except (TypeError, ValueError):
            raise serializers.ValidationError({
                "bead_size_mm": "Bead size must be a valid number."
            })

        if bead_size_mm not in self.ALLOWED_BEAD_SIZES:
            raise serializers.ValidationError({
                "bead_size_mm": (
                    "Invalid bead size. "
                    "Allowed sizes are 4, 6, 8 and 10 mm."
                )
            })

        # =====================================================
        # VERIFY EACH BEAD
        # =====================================================

        for index, bead_config in enumerate(beads):

            if not isinstance(bead_config, dict):
                raise serializers.ValidationError({
                    "beads": (
                        f"Bead #{index + 1} must be an object."
                    )
                })

            # -------------------------------------------------
            # BEAD ID
            # -------------------------------------------------

            if not bead_config.get("bead_id"):
                raise serializers.ValidationError({
                    "beads": (
                        f"bead_id is required "
                        f"for bead #{index + 1}."
                    )
                })

            try:
                Bead.objects.get(
                    id=bead_config["bead_id"]
                )

            except Bead.DoesNotExist:
                raise serializers.ValidationError({
                    "beads": (
                        f"Bead ID {bead_config['bead_id']} "
                        "does not exist."
                    )
                })

            # -------------------------------------------------
            # COLOR ID
            # -------------------------------------------------

            color_id = bead_config.get("color_id")

            if color_id is not None:

                try:
                    Color.objects.get(
                        id=color_id
                    )

                except Color.DoesNotExist:
                    raise serializers.ValidationError({
                        "beads": (
                            f"Color ID {color_id} "
                            "does not exist."
                        )
                    })

            # -------------------------------------------------
            # BEAD SIZE
            # -------------------------------------------------

            size_mm = bead_config.get("size_mm")

            if size_mm is None:
                raise serializers.ValidationError({
                    "beads": (
                        f"size_mm is required "
                        f"for bead #{index + 1}."
                    )
                })

            try:
                size_mm = int(size_mm)

            except (TypeError, ValueError):
                raise serializers.ValidationError({
                    "beads": (
                        f"Invalid size_mm "
                        f"for bead #{index + 1}."
                    )
                })

            if size_mm not in self.ALLOWED_BEAD_SIZES:
                raise serializers.ValidationError({
                    "beads": (
                        f"Invalid size_mm "
                        f"for bead #{index + 1}. "
                        "Allowed sizes are "
                        "4, 6, 8 and 10 mm."
                    )
                })

            # -------------------------------------------------
            # SAME SIZE FOR ALL BEADS
            # -------------------------------------------------

            if size_mm != bead_size_mm:
                raise serializers.ValidationError({
                    "beads": (
                        "All beads must have "
                        "the same size. "
                        f"Expected {bead_size_mm}mm "
                        f"but bead #{index + 1} "
                        f"has {size_mm}mm."
                    )
                })

        # =====================================================
        # DISK
        # =====================================================

        disk_id = configuration.get("disk_id")

        if not disk_id:
            raise serializers.ValidationError({
                "disk_id": "disk_id is required."
            })

        try:
            Disk.objects.get(
                id=disk_id
            )

        except Disk.DoesNotExist:
            raise serializers.ValidationError({
                "disk_id": (
                    f"Disk ID {disk_id} "
                    "does not exist."
                )
            })

        # =====================================================
        # FRAME
        # =====================================================

        if not configuration.get("frame_shape"):
            raise serializers.ValidationError({
                "frame_shape": (
                    "frame_shape is required."
                )
            })

        # =====================================================
        # MATERIAL
        # =====================================================

        if not configuration.get("material"):
            raise serializers.ValidationError({
                "material": (
                    "material is required."
                )
            })

        return configuration

    # =========================================================
    # CALCULATE TOTAL
    # =========================================================

    def calculate_total(
        self,
        bracelet,
        configuration,
        engraving,
        quantity
    ):

        # =====================================================
        # BASE BRACELET
        # =====================================================

        total = Decimal("149.00")

        # =====================================================
        # BEADS
        # =====================================================

        for bead_config in configuration["beads"]:

            bead_id = bead_config["bead_id"]
            color_id = bead_config.get("color_id")

            # Bois
            if bead_id == 1 and color_id is None:
                total += Decimal("2.50")

            # Colorées
            elif bead_id == 1 and color_id is not None:
                total += Decimal("3.25")

            # PVC
            elif bead_id == 2 and color_id is None:
                total += Decimal("3.50")

            # Argentées
            elif bead_id == 2 and color_id is not None:
                total += Decimal("5.50")

            # Roche
            elif bead_id == 3:
                total += Decimal("4.00")

        # =====================================================
        # DISK
        # =====================================================

        disk = Disk.objects.get(
            id=configuration["disk_id"]
        )

        disk_prices = {
            "circle": Decimal("3.00"),
            "octa": Decimal("4.00"),
            "capsule": Decimal("5.00"),
        }

        if disk.model not in disk_prices:
            raise serializers.ValidationError({
                "disk_id": (
                    "Invalid disk model. "
                    "Allowed models are circle, octa and capsule."
                )
            })

        total += disk_prices[disk.model]

        # =====================================================
        # ENGRAVING
        # =====================================================

        if engraving:
            total += Decimal("30.00")

        # =====================================================
        # QUANTITY
        # =====================================================

        total *= Decimal(str(quantity))

        return total

    # =========================================================
    # CREATE
    # =========================================================

    def create(self, validated_data):

        configuration = validated_data["configuration"]
        beads_config = configuration["beads"]

        # First bead
        first_bead = Bead.objects.get(
            id=beads_config[0]["bead_id"]
        )

        # First color
        first_color_id = beads_config[0].get("color_id")

        if first_color_id:
            first_color = Color.objects.get(
                id=first_color_id
            )
        else:
            first_color = Color.objects.first()

        # Disk
        disk = Disk.objects.get(
            id=configuration["disk_id"]
        )

        # Bracelet
        bracelet = validated_data["bracelet"]

        # Quantity
        quantity = validated_data.get(
            "quantity",
            1
        )

        # Engraving
        engraving = validated_data.get(
            "engraving",
            ""
        )

        # Calculate total
        total = self.calculate_total(
            bracelet=bracelet,
            configuration=configuration,
            engraving=engraving,
            quantity=quantity
        )

        # Compatibility fields
        validated_data["bead"] = first_bead
        validated_data["color"] = first_color
        validated_data["disk"] = disk
        validated_data["total_price"] = total

        return super().create(
            validated_data
        )

    # =========================================================
    # UPDATE
    # =========================================================

    def update(
        self,
        instance,
        validated_data
    ):

        # Configuration
        configuration = validated_data.get(
            "configuration",
            instance.configuration
        )

        configuration = self.validate_configuration(
            configuration
        )

        # Quantity
        quantity = validated_data.get(
            "quantity",
            instance.quantity
        )

        # Engraving
        engraving = validated_data.get(
            "engraving",
            instance.engraving
        )

        # Beads
        beads_config = configuration.get(
            "beads",
            []
        )

        if not beads_config:
            raise serializers.ValidationError({
                "configuration": (
                    "At least one bead is required."
                )
            })

        # First bead
        first_bead = Bead.objects.get(
            id=beads_config[0]["bead_id"]
        )

        # First color
        first_color_id = beads_config[0].get(
            "color_id"
        )

        if first_color_id:
            first_color = Color.objects.get(
                id=first_color_id
            )
        else:
            first_color = instance.color

        # Disk
        disk = Disk.objects.get(
            id=configuration["disk_id"]
        )

        # Calculate total
        total = self.calculate_total(
            bracelet=instance.bracelet,
            configuration=configuration,
            engraving=engraving,
            quantity=quantity
        )

        # Update compatibility fields
        validated_data["bead"] = first_bead
        validated_data["color"] = first_color
        validated_data["disk"] = disk
        validated_data["total_price"] = total

        return super().update(
            instance,
            validated_data
        )