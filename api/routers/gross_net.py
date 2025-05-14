from fastapi import APIRouter, HTTPException, Body, status
from core.calculator import calculate_gross_to_net
from core.models import GrossNetInput, GrossNetResult

router = APIRouter()

@router.post(
    "/gross-to-net",
    response_model=GrossNetResult,
    summary="Calculate Net Income from Gross Income",
    description="Calculates Vietnamese Net income, PIT, and insurance contributions based on Gross Income, Number of Dependents, and Region for April 2025 regulations.",
    tags=["Calculations"]
)
async def api_calculate_gross_to_net(
    input_data: GrossNetInput = Body(
        ...,
        examples={...}  # Giữ nguyên phần ví dụ
    )
):
    try:
        result = calculate_gross_to_net(input_data)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Input validation error: {str(e)}"
        )
    except Exception as e:
        print(f"ERROR: api_calculate_gross_to_net - {type(e).__name__}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred while processing the calculation."
        )

# Thêm phương thức HEAD
@router.head(
    "/gross-to-net",
    summary="Check availability of Gross-to-Net API",
    tags=["Calculations"]
)
async def head_gross_to_net():
    """
    This endpoint will respond to a HEAD request to check the availability of the Gross-to-Net calculation API.
    """
    return {"message": "API is available"}

# Thêm phương thức GET
@router.get(
    "/gross-to-net",
    response_model=GrossNetResult,
    summary="Get example calculation for Gross-to-Net",
    tags=["Calculations"]
)
async def get_gross_to_net_example():
    """
    This endpoint will return an example of Gross-to-Net calculation.
    It's a GET method to retrieve the example without making any calculations.
    """
    example_data = {
        "gross_income": 30000000,
        "num_dependents": 1,
        "region": 1
    }
    result = calculate_gross_to_net(example_data)  # Calculate the result using the same function
    return result
